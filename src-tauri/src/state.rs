use std::collections::HashMap;
use std::path::PathBuf;

use serde_json::Value;
use tokio::sync::Mutex;

use crate::framework::FrameworkManager;

pub struct AppState {
    pub framework: Mutex<FrameworkManager>,
    pub notebook_path: Mutex<Option<PathBuf>>,
    /// History of opened notebooks (most recent last)
    pub notebook_history: Mutex<Vec<PathBuf>>,
    pub pending: Mutex<HashMap<String, tokio::sync::oneshot::Sender<Value>>>,
    /// Page load counter (incremented each time bridge.js initializes)
    pub page_load_count: std::sync::atomic::AtomicU64,
    /// Timestamp of last page load (ms since epoch)
    pub last_page_load: std::sync::atomic::AtomicU64,
}

impl AppState {
    pub fn new(project_dir: PathBuf) -> Self {
        Self {
            framework: Mutex::new(FrameworkManager::new(project_dir)),
            notebook_path: Mutex::new(None),
            notebook_history: Mutex::new(Vec::new()),
            pending: Mutex::new(HashMap::new()),
            page_load_count: std::sync::atomic::AtomicU64::new(0),
            last_page_load: std::sync::atomic::AtomicU64::new(0),
        }
    }

    /// Add a notebook to history (moves to end if already present)
    pub async fn add_to_history(&self, path: PathBuf) {
        let mut history = self.notebook_history.lock().await;
        // Remove if already present (we'll re-add at the end)
        history.retain(|p| p != &path);
        history.push(path);
    }

    /// Get the notebook history (most recent last)
    pub async fn get_history(&self) -> Vec<PathBuf> {
        self.notebook_history.lock().await.clone()
    }
}
