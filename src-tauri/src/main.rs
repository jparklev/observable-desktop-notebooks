mod api;
mod bridge;
mod framework;
mod screenshot;
mod state;

fn main() {
    tauri::Builder::default()
        .setup(|app| {
            let app_handle = app.handle().clone();
            tauri::async_runtime::spawn(async move {
                if let Err(err) = api::serve(app_handle.clone()).await {
                    eprintln!("api server error: {err:#}");
                    app_handle.exit(1);
                }
            });

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
