use std::{io::Cursor, path::PathBuf, ptr::NonNull};

use anyhow::{Context, Result, anyhow};
use block2::RcBlock;
use image::GenericImageView;
use objc2::rc::Retained;
use objc2::runtime::AnyObject;
use objc2_app_kit::{NSBitmapImageFileType, NSBitmapImageRep, NSImage};
use objc2_foundation::{NSData, NSDictionary, NSError};
use objc2_web_kit::WKWebView;
use tauri::WebviewWindow;
use uuid::Uuid;

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
    let png = capture_png(window).await?;

    let img = image::load_from_memory(&png).context("decode png")?;
    let (img_w, img_h) = img.dimensions();
    let scale_x = (img_w as f64) / viewport.width.max(1.0);
    let scale_y = (img_h as f64) / viewport.height.max(1.0);

    let x0 = ((rect.x - padding_css_px) * scale_x).floor().max(0.0) as u32;
    let y0 = ((rect.y - padding_css_px) * scale_y).floor().max(0.0) as u32;
    let w = ((rect.width + 2.0 * padding_css_px) * scale_x)
        .ceil()
        .max(1.0) as u32;
    let h = ((rect.height + 2.0 * padding_css_px) * scale_y)
        .ceil()
        .max(1.0) as u32;

    let x0 = x0.min(img_w.saturating_sub(1));
    let y0 = y0.min(img_h.saturating_sub(1));
    let w = w.min(img_w.saturating_sub(x0)).max(1);
    let h = h.min(img_h.saturating_sub(y0)).max(1);

    let cropped = img.crop_imm(x0, y0, w, h);
    let mut out = Vec::new();
    cropped
        .write_to(&mut Cursor::new(&mut out), image::ImageFormat::Png)
        .context("encode cropped png")?;

    let path = write_temp_png(&out)?;
    Ok(path.display().to_string())
}

async fn capture_png(window: &WebviewWindow) -> Result<Vec<u8>> {
    #[cfg(not(target_os = "macos"))]
    {
        let _ = window;
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

            let block = RcBlock::new(move |image: *mut NSImage, err: *mut NSError| {
                let result = unsafe { snapshot_to_png(image, err) };
                let _ = tx.lock().ok().and_then(|mut tx| tx.take()).map(|tx| {
                    tx.send(result).ok();
                });
            });

            unsafe {
                wk.takeSnapshotWithConfiguration_completionHandler(None, &block);
            }
        })?;

        rx.await
            .map_err(|_| anyhow!("snapshot callback dropped"))?
            .context("snapshot failed")
    }
}

#[cfg(target_os = "macos")]
unsafe fn snapshot_to_png(image: *mut NSImage, err: *mut NSError) -> Result<Vec<u8>> {
    if !err.is_null() {
        return Err(anyhow!("WKWebView snapshot returned an error"));
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
