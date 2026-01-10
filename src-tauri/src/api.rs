use std::{
    ffi::OsStr,
    net::SocketAddr,
    path::{Path, PathBuf},
    sync::Arc,
};

use anyhow::Result;
use axum::{
    Router,
    extract::{Json, Path as AxumPath, State},
    http::StatusCode,
    response::IntoResponse,
    routing::{get, post},
};
use serde::{Deserialize, Serialize};
use serde_json::Value;
use tauri::{AppHandle, Manager};
use tower_http::cors::CorsLayer;
use uuid::Uuid;

use crate::{bridge, screenshot, state::AppState};

const DEFAULT_PORT: u16 = 9847;
const JS_TIMEOUT_MS: u64 = 5000;

#[derive(Clone)]
struct ApiState {
    app: AppHandle,
    state: Arc<AppState>,
}

pub async fn serve(app_handle: AppHandle) -> Result<()> {
    let notebooks_dir = project_notebooks_dir().unwrap_or_else(|| PathBuf::from("notebooks"));
    let state = Arc::new(AppState::new(notebooks_dir));
    let api_state = ApiState {
        app: app_handle,
        state,
    };

    let app = Router::new()
        .route("/status", get(status))
        .route("/notebook", get(get_notebook))
        .route("/notebooks", get(list_notebooks))
        .route("/cells", get(list_cells))
        .route("/cell/{name}", get(get_cell))
        .route("/logs", get(get_logs))
        .route("/input", post(set_input))
        .route("/click", post(click_element))
        .route("/open", post(open))
        .route("/close", post(close))
        .route("/reload", post(reload))
        .route("/window/show", post(window_show))
        .route("/window/hide", post(window_hide))
        .route("/shutdown", post(shutdown))
        .route("/eval", post(eval_js))
        .route("/wait-idle", post(wait_idle))
        .route("/screenshot", post(screenshot_full))
        .route("/screenshot/element", post(screenshot_element))
        .route("/verify", post(verify_notebook))
        .route("/_internal/reply", post(internal_reply))
        .route("/_internal/loaded", post(internal_loaded))
        .route("/page-loads", get(page_loads))
        .layer(CorsLayer::permissive())
        .with_state(api_state);

    let addr = SocketAddr::from(([127, 0, 0, 1], DEFAULT_PORT));
    let listener = tokio::net::TcpListener::bind(addr).await?;
    axum::serve(listener, app).await?;
    Ok(())
}

fn project_notebooks_dir() -> Option<PathBuf> {
    // App is in src-tauri; notebooks live at repo root.
    let cwd = std::env::current_dir().ok()?;
    let root = if cwd.ends_with("src-tauri") {
        cwd.parent()?.to_path_buf()
    } else {
        cwd
    };
    Some(root.join("notebooks"))
}

#[derive(Serialize)]
struct StatusResponse {
    ok: bool,
    framework_port: Option<u16>,
    notebook: Option<String>,
    busy: bool,
}

async fn status(State(api): State<ApiState>) -> impl IntoResponse {
    let mut busy = false;
    let port = match api.state.framework.try_lock() {
        Ok(framework) => framework.port(),
        Err(_) => {
            busy = true;
            None
        }
    };
    let notebook = api.state.notebook_path.lock().await.clone();
    Json(StatusResponse {
        ok: true,
        framework_port: port,
        notebook: notebook.map(|p| p.display().to_string()),
        busy,
    })
}

async fn get_notebook(State(api): State<ApiState>) -> impl IntoResponse {
    let notebook = api.state.notebook_path.lock().await.clone();
    Json(serde_json::json!({
        "ok": true,
        "path": notebook.map(|p| p.display().to_string())
    }))
}

async fn list_notebooks(State(api): State<ApiState>) -> impl IntoResponse {
    let current = api.state.notebook_path.lock().await.clone();
    let history = api.state.get_history().await;
    Json(serde_json::json!({
        "ok": true,
        "current": current.map(|p| p.display().to_string()),
        "history": history.iter().map(|p| p.display().to_string()).collect::<Vec<_>>()
    }))
}

async fn list_cells(State(api): State<ApiState>) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    let result = run_js(
        &api,
        &window,
        "return window.__notebook_viewer__?.listCells?.() ?? [];",
        JS_TIMEOUT_MS,
    )
    .await?;
    Ok(Json(serde_json::json!({ "ok": true, "cells": result })))
}

async fn get_cell(
    State(api): State<ApiState>,
    AxumPath(name): AxumPath<String>,
) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    let name = serde_json::to_string(&name).map_err(|e| ApiError(e.into()))?;
    let code = format!("return window.__notebook_viewer__?.getCellValue?.({name}) ?? null;");
    let result = run_js(&api, &window, &code, JS_TIMEOUT_MS).await?;
    Ok(Json(serde_json::json!({ "ok": true, "value": result })))
}

#[derive(Deserialize)]
struct LogsQuery {
    #[serde(default)]
    clear: bool,
}

async fn get_logs(
    State(api): State<ApiState>,
    axum::extract::Query(query): axum::extract::Query<LogsQuery>,
) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    let clear = if query.clear { "true" } else { "false" };
    let code = format!("return window.__notebook_viewer__?.getLogs?.({clear}) ?? [];");
    let result = run_js(&api, &window, &code, JS_TIMEOUT_MS).await?;
    Ok(Json(serde_json::json!({ "ok": true, "logs": result })))
}

#[derive(Deserialize)]
struct SetInputRequest {
    selector: String,
    value: Value,
}

async fn set_input(
    State(api): State<ApiState>,
    Json(req): Json<SetInputRequest>,
) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    let selector = serde_json::to_string(&req.selector).map_err(|e| ApiError(e.into()))?;
    let value = serde_json::to_string(&req.value).map_err(|e| ApiError(e.into()))?;
    let code = format!("return window.__notebook_viewer__?.setInputValue?.({selector}, {value});");
    let result = run_js(&api, &window, &code, JS_TIMEOUT_MS).await?;
    Ok(Json(serde_json::json!({ "ok": true, "result": result })))
}

#[derive(Deserialize)]
struct ClickRequest {
    selector: String,
}

async fn click_element(
    State(api): State<ApiState>,
    Json(req): Json<ClickRequest>,
) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    let selector = serde_json::to_string(&req.selector).map_err(|e| ApiError(e.into()))?;
    let code = format!("return window.__notebook_viewer__?.clickElement?.({selector});");
    let result = run_js(&api, &window, &code, JS_TIMEOUT_MS).await?;
    Ok(Json(serde_json::json!({ "ok": true, "result": result })))
}

#[derive(Deserialize)]
struct OpenRequest {
    path: String,
}

#[derive(Serialize)]
struct OpenResponse {
    ok: bool,
    framework_port: u16,
    url: String,
}

async fn open(
    State(api): State<ApiState>,
    Json(req): Json<OpenRequest>,
) -> Result<impl IntoResponse, ApiError> {
    let path = PathBuf::from(req.path);
    *api.state.notebook_path.lock().await = Some(path.clone());
    api.state.add_to_history(path.clone()).await;

    let mut framework = api.state.framework.lock().await;
    let port = framework.start().await.map_err(ApiError)?;
    let url = notebook_url(&framework, port, &path).map_err(ApiError)?;
    drop(framework);
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;

    bridge::navigate_to(&window, &url).map_err(ApiError)?;
    silent_show(&window).map_err(ApiError)?;
    Ok(Json(OpenResponse {
        ok: true,
        framework_port: port,
        url,
    }))
}

fn notebook_url(
    framework: &crate::framework::FrameworkManager,
    framework_port: u16,
    notebook_path: &Path,
) -> Result<String> {
    // Map: notebooks/src/foo.md -> /foo
    //      notebooks/src/index.md -> /
    //      notebooks/src/a/b.md -> /a/b
    //      notebooks/src/a/index.md -> /a
    let src_dir = framework.project_dir().join("src");
    let rel = notebook_path
        .strip_prefix(&src_dir)
        .unwrap_or(notebook_path);
    if rel.extension() != Some(OsStr::new("md")) {
        return Err(anyhow::anyhow!("expected .md notebook path"));
    }
    let rel = rel.with_extension("");

    let route = rel
        .to_string_lossy()
        .replace('\\', "/")
        .trim_end_matches("/index")
        .to_string();
    let route = if route == "index" {
        String::new()
    } else {
        route
    };
    let route = route.trim_matches('/').to_string();

    if route.is_empty() {
        Ok(format!("http://localhost:{framework_port}/"))
    } else {
        Ok(format!("http://localhost:{framework_port}/{route}"))
    }
}

async fn close(State(api): State<ApiState>) -> Result<impl IntoResponse, ApiError> {
    *api.state.notebook_path.lock().await = None;
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    bridge::navigate_to(&window, "about:blank").map_err(ApiError)?;
    window
        .set_skip_taskbar(true)
        .map_err(|e| ApiError(anyhow::anyhow!("set_skip_taskbar failed: {e}")))?;
    window
        .hide()
        .map_err(|e| ApiError(anyhow::anyhow!("hide failed: {e}")))?;
    Ok(Json(serde_json::json!({ "ok": true })))
}

async fn reload(State(api): State<ApiState>) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    window
        .reload()
        .map_err(|e| ApiError(anyhow::anyhow!("reload failed: {e}")))?;
    Ok(Json(serde_json::json!({ "ok": true })))
}

async fn window_show(State(api): State<ApiState>) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    window
        .set_skip_taskbar(false)
        .map_err(|e| ApiError(anyhow::anyhow!("set_skip_taskbar failed: {e}")))?;
    window
        .show()
        .map_err(|e| ApiError(anyhow::anyhow!("show failed: {e}")))?;
    window
        .center()
        .map_err(|e| ApiError(anyhow::anyhow!("center failed: {e}")))?;
    window
        .set_focus()
        .map_err(|e| ApiError(anyhow::anyhow!("set_focus failed: {e}")))?;
    Ok(Json(serde_json::json!({ "ok": true })))
}

async fn window_hide(State(api): State<ApiState>) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    silent_show(&window).map_err(ApiError)?;
    Ok(Json(serde_json::json!({ "ok": true })))
}

fn silent_show(window: &tauri::WebviewWindow) -> anyhow::Result<()> {
    window
        .set_skip_taskbar(true)
        .map_err(|e| anyhow::anyhow!("set_skip_taskbar failed: {e}"))?;
    window
        .set_position(tauri::PhysicalPosition::new(-10_000, -10_000))
        .map_err(|e| anyhow::anyhow!("set_position failed: {e}"))?;
    window
        .show()
        .map_err(|e| anyhow::anyhow!("show failed: {e}"))?;
    Ok(())
}

async fn shutdown(State(api): State<ApiState>) -> Result<impl IntoResponse, ApiError> {
    {
        let mut framework = api.state.framework.lock().await;
        framework
            .stop()
            .await
            .map_err(|e| ApiError(anyhow::anyhow!("framework stop failed: {e}")))?;
    }

    // Exit on a short delay so the HTTP response flushes.
    let app = api.app.clone();
    tokio::spawn(async move {
        tokio::time::sleep(std::time::Duration::from_millis(50)).await;
        app.exit(0);
    });

    Ok(Json(serde_json::json!({ "ok": true })))
}

#[derive(Deserialize)]
struct EvalRequest {
    code: String,
    timeout_ms: Option<u64>,
}

async fn eval_js(
    State(api): State<ApiState>,
    Json(req): Json<EvalRequest>,
) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    let result = run_js(
        &api,
        &window,
        &req.code,
        req.timeout_ms.unwrap_or(JS_TIMEOUT_MS),
    )
    .await?;
    Ok(Json(serde_json::json!({ "ok": true, "result": result })))
}

#[derive(Deserialize)]
struct WaitIdleRequest {
    timeout_ms: Option<u64>,
}

async fn wait_idle(
    State(api): State<ApiState>,
    Json(req): Json<WaitIdleRequest>,
) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    let timeout_ms = req.timeout_ms.unwrap_or(5000);
    let result = wait_idle_js(&api, &window, timeout_ms).await?;
    Ok(Json(serde_json::json!({ "ok": true, "result": result })))
}

async fn internal_reply(
    State(api): State<ApiState>,
    Json(payload): Json<Value>,
) -> Result<impl IntoResponse, ApiError> {
    let id = payload
        .get("id")
        .and_then(|v| v.as_str())
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing id")))?
        .to_string();

    if let Some(tx) = api.state.pending.lock().await.remove(&id) {
        if tx.send(payload).is_err() {
            eprintln!("internal_reply: channel closed for id={id}");
        }
    } else {
        eprintln!("internal_reply: no pending request for id={id}");
    }

    Ok(Json(serde_json::json!({ "ok": true })))
}

async fn internal_loaded(State(api): State<ApiState>) -> impl IntoResponse {
    use std::sync::atomic::Ordering;
    use std::time::{SystemTime, UNIX_EPOCH};

    api.state.page_load_count.fetch_add(1, Ordering::SeqCst);
    let now = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map(|d| d.as_millis() as u64)
        .unwrap_or(0);
    api.state.last_page_load.store(now, Ordering::SeqCst);

    Json(serde_json::json!({ "ok": true }))
}

async fn page_loads(State(api): State<ApiState>) -> impl IntoResponse {
    use std::sync::atomic::Ordering;

    let count = api.state.page_load_count.load(Ordering::SeqCst);
    let last = api.state.last_page_load.load(Ordering::SeqCst);

    Json(serde_json::json!({
        "ok": true,
        "count": count,
        "last_load_ms": last
    }))
}

async fn run_js(
    api: &ApiState,
    window: &tauri::WebviewWindow,
    code: &str,
    timeout_ms: u64,
) -> Result<Value, ApiError> {
    let id = Uuid::new_v4().to_string();
    let (tx, rx) = tokio::sync::oneshot::channel::<Value>();
    api.state.pending.lock().await.insert(id.clone(), tx);

    bridge::dispatch_eval(window, DEFAULT_PORT, &id, code).map_err(ApiError)?;
    let payload = match tokio::time::timeout(std::time::Duration::from_millis(timeout_ms), rx).await
    {
        Ok(Ok(payload)) => payload,
        Ok(Err(_)) => {
            api.state.pending.lock().await.remove(&id);
            return Err(ApiError(anyhow::anyhow!("JS reply channel closed")));
        }
        Err(_) => {
            api.state.pending.lock().await.remove(&id);
            return Err(ApiError(anyhow::anyhow!("timed out waiting for JS reply")));
        }
    };

    if payload.get("ok").and_then(|v| v.as_bool()) != Some(true) {
        let err = payload
            .get("error")
            .and_then(|v| v.as_str())
            .unwrap_or("unknown js error");
        return Err(ApiError(anyhow::anyhow!(err.to_string())));
    }

    Ok(payload.get("value").cloned().unwrap_or(Value::Null))
}

async fn wait_idle_js(
    api: &ApiState,
    window: &tauri::WebviewWindow,
    timeout_ms: u64,
) -> Result<Value, ApiError> {
    let id = Uuid::new_v4().to_string();
    let (tx, rx) = tokio::sync::oneshot::channel::<Value>();
    api.state.pending.lock().await.insert(id.clone(), tx);

    bridge::dispatch_wait_idle(window, DEFAULT_PORT, &id, timeout_ms).map_err(ApiError)?;
    let payload =
        match tokio::time::timeout(std::time::Duration::from_millis(timeout_ms + 250), rx).await {
            Ok(Ok(payload)) => payload,
            Ok(Err(_)) => {
                api.state.pending.lock().await.remove(&id);
                return Err(ApiError(anyhow::anyhow!("idle reply channel closed")));
            }
            Err(_) => {
                api.state.pending.lock().await.remove(&id);
                return Err(ApiError(anyhow::anyhow!(
                    "timed out waiting for idle reply"
                )));
            }
        };

    if payload.get("ok").and_then(|v| v.as_bool()) != Some(true) {
        let err = payload
            .get("error")
            .and_then(|v| v.as_str())
            .unwrap_or("unknown js error");
        return Err(ApiError(anyhow::anyhow!(err.to_string())));
    }

    Ok(payload.get("value").cloned().unwrap_or(Value::Null))
}

async fn screenshot_full(State(api): State<ApiState>) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;
    let path = screenshot::capture_window(&window)
        .await
        .map_err(ApiError)?;
    Ok(Json(serde_json::json!({ "ok": true, "path": path })))
}

#[derive(Deserialize)]
struct ScreenshotElementRequest {
    selector: String,
    padding: Option<u32>,
}

async fn screenshot_element(
    State(api): State<ApiState>,
    Json(req): Json<ScreenshotElementRequest>,
) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;

    #[derive(Deserialize)]
    struct Metrics {
        rect: Rect,
        viewport: Viewport,
    }

    #[derive(Deserialize)]
    struct Rect {
        x: f64,
        y: f64,
        width: f64,
        height: f64,
    }

    #[derive(Deserialize)]
    struct Viewport {
        width: f64,
        height: f64,
    }

    let selector = serde_json::to_string(&req.selector).map_err(|e| ApiError(e.into()))?;
    let padding = req.padding.unwrap_or(16);

    let code = format!(
        r#"
const selector = {selector};
const el = document.querySelector(selector);
if (!el) throw new Error("selector not found: " + selector);

// Calculate document position and scroll manually (scrollIntoView can overshoot)
const rect = el.getBoundingClientRect();
const docTop = window.scrollY + rect.top;
const targetY = docTop - (window.innerHeight - rect.height) / 2;
window.scrollTo(0, Math.max(0, targetY));

if (window.__notebook_viewer__?.waitForIdle) {{
  await window.__notebook_viewer__.waitForIdle(1500);
}}

const r = el.getBoundingClientRect();
return {{
  rect: {{x: r.x, y: r.y, width: r.width, height: r.height}},
  viewport: {{width: window.innerWidth, height: window.innerHeight}}
}};
"#
    );

    let value = run_js(&api, &window, &code, JS_TIMEOUT_MS).await?;
    let metrics: Metrics = serde_json::from_value(value).map_err(|e| ApiError(e.into()))?;

    let path = screenshot::capture_element(
        &window,
        screenshot::CssRect {
            x: metrics.rect.x,
            y: metrics.rect.y,
            width: metrics.rect.width,
            height: metrics.rect.height,
        },
        screenshot::CssViewport {
            width: metrics.viewport.width,
            height: metrics.viewport.height,
        },
        padding as f64,
    )
    .await
    .map_err(ApiError)?;
    Ok(Json(serde_json::json!({ "ok": true, "path": path })))
}

#[derive(Deserialize)]
struct VerifyRequest {
    timeout_ms: Option<u64>,
    screenshot_padding: Option<u32>,
}

#[derive(Serialize)]
struct VerifyVisualization {
    index: usize,
    #[serde(rename = "type")]
    viz_type: String,
    selector: Option<String>,
    size: [u32; 2],
    screenshot_path: String,
    context_text: Option<String>,
}

#[derive(Serialize)]
struct VerifyResponse {
    ok: bool,
    page_errors: Vec<String>,
    visualizations: Vec<VerifyVisualization>,
    inputs: usize,
    exposed_cells: Vec<String>,
}

async fn verify_notebook(
    State(api): State<ApiState>,
    Json(req): Json<VerifyRequest>,
) -> Result<impl IntoResponse, ApiError> {
    let window = api
        .app
        .get_webview_window("main")
        .ok_or_else(|| ApiError(anyhow::anyhow!("missing main window")))?;

    let timeout_ms = req.timeout_ms.unwrap_or(10000);
    let padding = req.screenshot_padding.unwrap_or(16) as f64;

    // 1. Wait for idle
    wait_idle_js(&api, &window, timeout_ms).await?;

    // 2. Get console errors
    let logs = run_js(&api, &window, "return window.__notebook_viewer__?.getLogs?.() ?? [];", JS_TIMEOUT_MS).await?;
    let page_errors: Vec<String> = logs
        .as_array()
        .map(|arr| {
            arr.iter()
                .filter_map(|entry| {
                    let level = entry.get("level")?.as_str()?;
                    if level == "error" {
                        entry.get("message")?.as_str().map(|s| s.to_string())
                    } else {
                        None
                    }
                })
                .collect()
        })
        .unwrap_or_default();

    // 3. Discover visualizations
    let viz_data = run_js(
        &api,
        &window,
        "return window.__notebook_viewer__?.discoverVisualizations?.() ?? [];",
        JS_TIMEOUT_MS,
    )
    .await?;

    // 4. Count inputs
    let input_count = run_js(
        &api,
        &window,
        "return document.querySelectorAll('input, select, textarea').length;",
        JS_TIMEOUT_MS,
    )
    .await?
    .as_u64()
    .unwrap_or(0) as usize;

    // 5. Get exposed cells
    let cells = run_js(
        &api,
        &window,
        "return window.__notebook_viewer__?.listCells?.() ?? [];",
        JS_TIMEOUT_MS,
    )
    .await?;
    let exposed_cells: Vec<String> = cells
        .as_array()
        .map(|arr| arr.iter().filter_map(|v| v.as_str().map(|s| s.to_string())).collect())
        .unwrap_or_default();

    // 6. Screenshot each visualization (sequential for speed, no duplicate scrolling)
    let mut visualizations = Vec::new();

    if let Some(viz_arr) = viz_data.as_array() {
        for viz in viz_arr {
            let index = viz.get("index").and_then(|v| v.as_u64()).unwrap_or(0) as usize;
            let viz_type = viz
                .get("type")
                .and_then(|v| v.as_str())
                .unwrap_or("unknown")
                .to_string();
            let selector = viz.get("selector").and_then(|v| v.as_str()).map(|s| s.to_string());
            let context_text = viz.get("contextText").and_then(|v| v.as_str()).map(|s| s.to_string());

            let rect = viz.get("rect");
            let width = rect
                .and_then(|r| r.get("width"))
                .and_then(|v| v.as_f64())
                .unwrap_or(0.0) as u32;
            let height = rect
                .and_then(|r| r.get("height"))
                .and_then(|v| v.as_f64())
                .unwrap_or(0.0) as u32;

            // Scroll to element and capture
            if let Some(ref sel) = selector {
                let sel_json = serde_json::to_string(sel).map_err(|e| ApiError(e.into()))?;
                let scroll_code = format!(
                    r#"
                    const el = document.querySelector({sel_json});
                    if (el) {{
                        // Calculate document position and scroll manually
                        // (scrollIntoView can overshoot on some pages)
                        const rect = el.getBoundingClientRect();
                        const docTop = window.scrollY + rect.top;
                        const targetY = docTop - (window.innerHeight - rect.height) / 2;
                        window.scrollTo(0, Math.max(0, targetY));
                        await new Promise(r => setTimeout(r, 50));
                        const r = el.getBoundingClientRect();
                        return {{
                            rect: {{x: r.x, y: r.y, width: r.width, height: r.height}},
                            viewport: {{width: window.innerWidth, height: window.innerHeight}}
                        }};
                    }}
                    return null;
                    "#
                );

                if let Ok(metrics_val) = run_js(&api, &window, &scroll_code, JS_TIMEOUT_MS).await {
                    if !metrics_val.is_null() {
                        #[derive(Deserialize)]
                        struct Metrics {
                            rect: Rect,
                            viewport: Viewport,
                        }
                        #[derive(Deserialize)]
                        struct Rect {
                            x: f64,
                            y: f64,
                            width: f64,
                            height: f64,
                        }
                        #[derive(Deserialize)]
                        struct Viewport {
                            width: f64,
                            height: f64,
                        }

                        if let Ok(metrics) = serde_json::from_value::<Metrics>(metrics_val) {
                            if let Ok(path) = screenshot::capture_element(
                                &window,
                                screenshot::CssRect {
                                    x: metrics.rect.x,
                                    y: metrics.rect.y,
                                    width: metrics.rect.width,
                                    height: metrics.rect.height,
                                },
                                screenshot::CssViewport {
                                    width: metrics.viewport.width,
                                    height: metrics.viewport.height,
                                },
                                padding,
                            )
                            .await
                            {
                                visualizations.push(VerifyVisualization {
                                    index,
                                    viz_type,
                                    selector,
                                    size: [width, height],
                                    screenshot_path: path,
                                    context_text,
                                });
                                continue;
                            }
                        }
                    }
                }
            }

            // Fallback: no screenshot captured
            visualizations.push(VerifyVisualization {
                index,
                viz_type,
                selector,
                size: [width, height],
                screenshot_path: String::new(),
                context_text,
            });
        }
    }

    Ok(Json(VerifyResponse {
        ok: true,
        page_errors,
        visualizations,
        inputs: input_count,
        exposed_cells,
    }))
}

struct ApiError(anyhow::Error);

impl IntoResponse for ApiError {
    fn into_response(self) -> axum::response::Response {
        (
            StatusCode::INTERNAL_SERVER_ERROR,
            Json(serde_json::json!({
                "ok": false,
                "error": self.0.to_string()
            })),
        )
            .into_response()
    }
}
