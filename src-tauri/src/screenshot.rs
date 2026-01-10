use std::{path::PathBuf, ptr::NonNull};

use anyhow::{Context, Result, anyhow};
use block2::RcBlock;
use objc2::MainThreadMarker;
use objc2::rc::Retained;
use objc2::runtime::AnyObject;
use objc2_app_kit::{NSBitmapImageFileType, NSBitmapImageRep, NSImage};
use objc2_core_foundation::{CGPoint, CGRect, CGSize};
use objc2_foundation::{NSData, NSDictionary, NSError};
use objc2_web_kit::{WKSnapshotConfiguration, WKWebView};
use tauri::WebviewWindow;
use uuid::Uuid;

const SNAPSHOT_TIMEOUT_ELEMENT_MS: u64 = 2000;
const SNAPSHOT_TIMEOUT_WINDOW_MS: u64 = 8000;

#[derive(Debug, Clone, Copy)]
pub struct CssRect {
    pub x: f64,
    pub y: f64,
    pub width: f64,
    pub height: f64,
}

#[derive(Debug, Clone, Copy)]
pub struct CssViewport {
    pub width: f64,
    pub height: f64,
}

pub async fn capture_window(window: &WebviewWindow) -> Result<String> {
    let png = capture_png(window).await?;
    let path = write_temp_png(&png)?;
    Ok(path.display().to_string())
}

pub async fn capture_element(
    window: &WebviewWindow,
    rect: CssRect,
    viewport: CssViewport,
    padding_css_px: f64,
) -> Result<String> {
    let viewport_w = viewport.width.max(0.0);
    let viewport_h = viewport.height.max(0.0);
    if viewport_w == 0.0 || viewport_h == 0.0 {
        return Err(anyhow!("invalid viewport size: {}x{}", viewport.width, viewport.height));
    }

    let x0 = (rect.x - padding_css_px).max(0.0);
    let y0 = (rect.y - padding_css_px).max(0.0);
    let x1 = (rect.x + rect.width + padding_css_px).min(viewport_w);
    let y1 = (rect.y + rect.height + padding_css_px).min(viewport_h);

    let w = (x1 - x0).max(1.0);
    let h = (y1 - y0).max(1.0);

    let rect = CssRect { x: x0, y: y0, width: w, height: h };
    let png = match capture_png_rect(window, rect, false).await {
        Ok(png) => png,
        Err(err) => {
            capture_png_rect(window, rect, true)
                .await
                .with_context(|| format!("snapshot failed (afterScreenUpdates=false): {err}"))?
        }
    };
    let path = write_temp_png(&png)?;
    Ok(path.display().to_string())
}

async fn capture_png(window: &WebviewWindow) -> Result<Vec<u8>> {
    capture_png_config(window, None, false, SNAPSHOT_TIMEOUT_WINDOW_MS).await
}

async fn capture_png_rect(
    window: &WebviewWindow,
    rect: CssRect,
    after_screen_updates: bool,
) -> Result<Vec<u8>> {
    capture_png_config(window, Some(rect), after_screen_updates, SNAPSHOT_TIMEOUT_ELEMENT_MS).await
}

async fn capture_png_config(
    window: &WebviewWindow,
    rect: Option<CssRect>,
    after_screen_updates: bool,
    timeout_ms: u64,
) -> Result<Vec<u8>> {
    #[cfg(not(target_os = "macos"))]
    {
        let _ = window;
        let _ = rect;
        let _ = after_screen_updates;
        let _ = timeout_ms;
        return Err(anyhow!("screenshot capture is only implemented on macOS"));
    }

    #[cfg(target_os = "macos")]
    {
        use tokio::sync::oneshot;

        let (tx, rx) = oneshot::channel::<Result<Vec<u8>>>();
        let tx = std::sync::Mutex::new(Some(tx));

        window.with_webview(move |webview| {
            let wk = unsafe { (webview.inner() as *mut WKWebView).as_ref() };
            let Some(wk) = wk else {
                let _ = tx.lock().ok().and_then(|mut tx| tx.take()).map(|tx| {
                    tx.send(Err(anyhow!("missing WKWebView handle"))).ok();
                });
                return;
            };

            let config = if let Some(rect) = rect {
                let mtm = MainThreadMarker::new();
                let Some(mtm) = mtm else {
                    let _ = tx.lock().ok().and_then(|mut tx| tx.take()).map(|tx| {
                        tx.send(Err(anyhow!("snapshot config requires main thread"))).ok();
                    });
                    return;
                };

                let config = unsafe { WKSnapshotConfiguration::new(mtm) };
                let rect =
                    CGRect::new(CGPoint::new(rect.x, rect.y), CGSize::new(rect.width, rect.height));
                unsafe {
                    config.setRect(rect);
                    config.setAfterScreenUpdates(after_screen_updates);
                }
                Some(config)
            } else {
                None
            };

            let block = RcBlock::new({
                let config = config.clone();
                move |image: *mut NSImage, err: *mut NSError| {
                    let _keep_alive = &config;
                    let result = unsafe { snapshot_to_png(image, err) };
                    let _ = tx.lock().ok().and_then(|mut tx| tx.take()).map(|tx| {
                        tx.send(result).ok();
                    });
                }
            });

            unsafe {
                wk.takeSnapshotWithConfiguration_completionHandler(config.as_deref(), &block);
            }
        })?;

        let result = tokio::time::timeout(std::time::Duration::from_millis(timeout_ms), rx)
            .await
            .map_err(|_| anyhow!("timed out waiting for snapshot callback"))?;
        result
            .map_err(|_| anyhow!("snapshot callback dropped"))?
            .context("snapshot failed")
    }
}

#[cfg(target_os = "macos")]
unsafe fn snapshot_to_png(image: *mut NSImage, err: *mut NSError) -> Result<Vec<u8>> {
    if !err.is_null() {
        let err = unsafe { err.as_ref() }.ok_or_else(|| anyhow!("snapshot error is null"))?;
        return Err(anyhow!("WKWebView snapshot returned an error: {err:?}"));
    }
    let image = unsafe { image.as_ref() }.ok_or_else(|| anyhow!("snapshot image is null"))?;

    let tiff: Retained<NSData> = image
        .TIFFRepresentation()
        .ok_or_else(|| anyhow!("snapshot image has no TIFF representation"))?;
    let rep: Retained<NSBitmapImageRep> =
        NSBitmapImageRep::imageRepWithData(&tiff).ok_or_else(|| anyhow!("TIFF decode failed"))?;

    let props: Retained<NSDictionary<objc2_app_kit::NSBitmapImageRepPropertyKey, AnyObject>> =
        NSDictionary::dictionary();
    let png: Retained<NSData> =
        unsafe { rep.representationUsingType_properties(NSBitmapImageFileType::PNG, &props) }
            .ok_or_else(|| anyhow!("PNG encode failed"))?;

    let len = png.length() as usize;
    let mut out = vec![0_u8; len];
    let ptr = NonNull::new(out.as_mut_ptr().cast()).ok_or_else(|| anyhow!("null buffer"))?;
    unsafe {
        png.getBytes_length(ptr, len as _);
    }
    Ok(out)
}

fn write_temp_png(bytes: &[u8]) -> Result<PathBuf> {
    let dir = std::env::temp_dir().join("notebook-viewer");
    if let Err(e) = std::fs::create_dir_all(&dir) {
        eprintln!("warning: failed to create screenshot directory {}: {e}", dir.display());
    }
    let path = dir.join(format!("screenshot-{}.png", Uuid::new_v4()));
    std::fs::write(&path, bytes).context("write screenshot png")?;
    Ok(path)
}
