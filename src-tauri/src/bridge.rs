use anyhow::{Result, anyhow};
use tauri::{Url, WebviewWindow};

const BRIDGE_JS: &str = include_str!("../../src/bridge.js");

pub fn navigate_to(window: &WebviewWindow, url: &str) -> Result<()> {
    let url = Url::parse(url).map_err(|e| anyhow!(e.to_string()))?;
    window.navigate(url)?;
    Ok(())
}

pub fn ensure_loaded(window: &WebviewWindow) -> Result<()> {
    window.eval(BRIDGE_JS)?;
    Ok(())
}

pub fn dispatch_eval(window: &WebviewWindow, api_port: u16, id: &str, code: &str) -> Result<()> {
    ensure_loaded(window)?;
    let id = serde_json::to_string(id)?;
    let code = serde_json::to_string(code)?;
    window.eval(format!(
        r#"(async () => {{
          try {{
            await window.__notebook_viewer__.evalAndPost({api_port}, {id}, {code});
          }} catch (err) {{
            try {{
              await fetch("http://127.0.0.1:{api_port}/_internal/reply", {{
                method: "POST",
                headers: {{ "content-type": "application/json" }},
                body: JSON.stringify({{ id: {id}, ok: false, error: String(err) }})
              }});
            }} catch (_) {{}}
          }}
        }})()"#
    ))?;
    Ok(())
}

pub fn dispatch_wait_idle(
    window: &WebviewWindow,
    api_port: u16,
    id: &str,
    timeout_ms: u64,
) -> Result<()> {
    ensure_loaded(window)?;
    let id = serde_json::to_string(id)?;
    window.eval(format!(
        r#"(async () => {{
          try {{
            await window.__notebook_viewer__.waitIdleAndPost({api_port}, {id}, {timeout_ms});
          }} catch (err) {{
            try {{
              await fetch("http://127.0.0.1:{api_port}/_internal/reply", {{
                method: "POST",
                headers: {{ "content-type": "application/json" }},
                body: JSON.stringify({{ id: {id}, ok: false, error: String(err) }})
              }});
            }} catch (_) {{}}
          }}
        }})()"#
    ))?;
    Ok(())
}
