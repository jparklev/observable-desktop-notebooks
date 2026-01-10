use std::{io::ErrorKind, net::TcpListener, path::PathBuf, process::Stdio, time::Duration};

use anyhow::{Context, Result, anyhow};
use tokio::{
    io::{AsyncBufReadExt, BufReader},
    net::TcpStream,
    process::{Child, Command},
    sync::mpsc,
    time::sleep,
};

pub struct FrameworkManager {
    child: Option<Child>,
    port: Option<u16>,
    pgid: Option<i32>,
    project_dir: PathBuf,
}

impl FrameworkManager {
    pub fn new(project_dir: PathBuf) -> Self {
        Self {
            child: None,
            port: None,
            pgid: None,
            project_dir,
        }
    }

    pub fn port(&self) -> Option<u16> {
        self.port
    }

    pub fn project_dir(&self) -> &PathBuf {
        &self.project_dir
    }

    pub async fn start(&mut self) -> Result<u16> {
        if let (Some(port), Some(child)) = (self.port, self.child.as_mut()) {
            if child.try_wait().context("poll preview process")?.is_none() {
                return Ok(port);
            }
            self.port = None;
            self.child = None;
            self.pgid = None;
        }

        // Retry with different ports in case of TOCTOU race
        const MAX_PORT_RETRIES: usize = 3;
        let mut all_errors: Vec<String> = Vec::new();

        for attempt in 0..MAX_PORT_RETRIES {
            let port = pick_port()?;
            let mut errors: Vec<String> = Vec::new();

            for cmd in preview_commands(port) {
                match spawn_preview(&self.project_dir, &cmd, port).await {
                    Ok(preview) => {
                        self.pgid = preview.pgid;
                        self.child = Some(preview.child);
                        self.port = Some(port);
                        return Ok(port);
                    }
                    Err(err) => errors.push(format!("{}: {err:#}", cmd.display_name())),
                }
            }

            all_errors.push(format!("attempt {} (port {}): {}", attempt + 1, port, errors.join("; ")));
        }

        Err(anyhow!(
            "failed to start Observable Framework preview server after {} attempts:\n{}",
            MAX_PORT_RETRIES,
            all_errors.join("\n")
        ))
    }

    pub async fn stop(&mut self) -> Result<()> {
        self.port = None;
        let pgid = self.pgid.take();
        if let Some(mut child) = self.child.take() {
            let pid = child.id().map(|id| id as i32);
            terminate_process_group(pgid);
            terminate_process(pid);

            match tokio::time::timeout(Duration::from_secs(3), child.wait()).await {
                Ok(_) => {}
                Err(_) => {
                    kill_process_group(pgid);
                    kill_process(pid);
                    let _ = tokio::time::timeout(Duration::from_secs(1), child.wait()).await;
                }
            }
        }
        Ok(())
    }
}

impl Drop for FrameworkManager {
    fn drop(&mut self) {
        terminate_process_group(self.pgid);
        if let Some(mut child) = self.child.take() {
            let _ = child.start_kill();
        }
    }
}

struct PreviewCommand {
    program: String,
    args: Vec<String>,
}

impl PreviewCommand {
    fn display_name(&self) -> String {
        let mut s = self.program.clone();
        for arg in &self.args {
            s.push(' ');
            s.push_str(arg);
        }
        s
    }
}

fn preview_commands(port: u16) -> Vec<PreviewCommand> {
    vec![
        PreviewCommand {
            program: "fnm".to_string(),
            args: vec![
                "exec".to_string(),
                "--using".to_string(),
                "22".to_string(),
                "--".to_string(),
                "./node_modules/.bin/observable".to_string(),
                "preview".to_string(),
                "--port".to_string(),
                port.to_string(),
                "--no-open".to_string(),
            ],
        },
        PreviewCommand {
            program: "./node_modules/.bin/observable".to_string(),
            args: vec![
                "preview".to_string(),
                "--port".to_string(),
                port.to_string(),
                "--no-open".to_string(),
            ],
        },
        PreviewCommand {
            program: "npx".to_string(),
            args: vec![
                "--yes".to_string(),
                "observable".to_string(),
                "preview".to_string(),
                "--port".to_string(),
                port.to_string(),
                "--no-open".to_string(),
            ],
        },
    ]
}

struct SpawnedPreview {
    child: Child,
    pgid: Option<i32>,
}

async fn spawn_preview(project_dir: &PathBuf, cmd: &PreviewCommand, port: u16) -> Result<SpawnedPreview> {
    let mut command = Command::new(&cmd.program);
    command
        .current_dir(project_dir)
        .args(&cmd.args)
        .stdout(Stdio::piped())
        .stderr(Stdio::piped());
    configure_process_group(&mut command);

    let mut child = match command.spawn() {
        Ok(child) => child,
        Err(err) if err.kind() == ErrorKind::NotFound => {
            return Err(anyhow!("command not found"));
        }
        Err(err) => return Err(err).with_context(|| cmd.display_name()),
    };

    let pgid = child.id().map(|id| id as i32);

    let mut logs: Vec<String> = Vec::new();
    let (tx, mut rx) = mpsc::unbounded_channel::<String>();

    if let Some(stdout) = child.stdout.take() {
        let tx = tx.clone();
        tokio::spawn(async move {
            let mut lines = BufReader::new(stdout).lines();
            while let Ok(Some(line)) = lines.next_line().await {
                let _ = tx.send(line);
            }
        });
    }

    if let Some(stderr) = child.stderr.take() {
        let tx = tx.clone();
        tokio::spawn(async move {
            let mut lines = BufReader::new(stderr).lines();
            while let Ok(Some(line)) = lines.next_line().await {
                let _ = tx.send(line);
            }
        });
    }

    let addr = format!("127.0.0.1:{port}");
    for _ in 0..400 {
        while let Ok(line) = rx.try_recv() {
            if logs.len() >= 16 {
                logs.remove(0);
            }
            logs.push(line);
        }

        if TcpStream::connect(&addr).await.is_ok() {
            return Ok(SpawnedPreview { child, pgid });
        }

        if let Some(status) = child.try_wait().context("poll preview process")? {
            return Err(anyhow!(
                "preview process exited ({status}); output:\n{}",
                logs.join("\n")
            ));
        }

        sleep(Duration::from_millis(50)).await;
    }

    terminate_process_group(pgid);
    child.start_kill().ok();
    Err(anyhow!(
        "preview port {port} did not open; last output:\n{}",
        logs.join("\n")
    ))
}

/// Pick an available port by binding to :0 and keeping the listener open until we return.
/// This minimizes the TOCTOU window but doesn't eliminate it entirely since we must
/// close the socket before Observable Framework can bind to it.
fn pick_port() -> Result<u16> {
    let listener = TcpListener::bind(("127.0.0.1", 0)).context("bind ephemeral port")?;
    let port = listener.local_addr()?.port();
    // Set SO_REUSEADDR so the port can be reused immediately after we drop the listener
    #[cfg(unix)]
    {
        use std::os::unix::io::AsRawFd;
        let fd = listener.as_raw_fd();
        unsafe {
            let optval: libc::c_int = 1;
            libc::setsockopt(
                fd,
                libc::SOL_SOCKET,
                libc::SO_REUSEADDR,
                &optval as *const _ as *const libc::c_void,
                std::mem::size_of::<libc::c_int>() as libc::socklen_t,
            );
        }
    }
    Ok(port)
}

fn configure_process_group(command: &mut Command) {
    #[cfg(unix)]
    {
        use std::os::unix::process::CommandExt;

        command.as_std_mut().process_group(0);
    }
}

fn terminate_process_group(pgid: Option<i32>) {
    #[cfg(unix)]
    {
        if let Some(pgid) = pgid {
            if let Err(e) = signal_process_group(pgid, libc::SIGTERM) {
                eprintln!("warning: failed to send SIGTERM to process group {pgid}: {e}");
            }
        }
    }
}

fn kill_process_group(pgid: Option<i32>) {
    #[cfg(unix)]
    {
        if let Some(pgid) = pgid {
            if let Err(e) = signal_process_group(pgid, libc::SIGKILL) {
                eprintln!("warning: failed to send SIGKILL to process group {pgid}: {e}");
            }
        }
    }
}

fn terminate_process(pid: Option<i32>) {
    #[cfg(unix)]
    {
        if let Some(pid) = pid {
            if let Err(e) = signal_process(pid, libc::SIGTERM) {
                eprintln!("warning: failed to send SIGTERM to process {pid}: {e}");
            }
        }
    }
}

fn kill_process(pid: Option<i32>) {
    #[cfg(unix)]
    {
        if let Some(pid) = pid {
            if let Err(e) = signal_process(pid, libc::SIGKILL) {
                eprintln!("warning: failed to send SIGKILL to process {pid}: {e}");
            }
        }
    }
}

#[cfg(unix)]
fn signal_process(pid: i32, signal: i32) -> std::io::Result<()> {
    let rc = unsafe { libc::kill(pid, signal) };
    if rc == 0 {
        return Ok(());
    }
    let err = std::io::Error::last_os_error();
    if err.raw_os_error() == Some(libc::ESRCH) {
        return Ok(());
    }
    Err(err)
}

#[cfg(unix)]
fn signal_process_group(pgid: i32, signal: i32) -> std::io::Result<()> {
    let rc = unsafe { libc::kill(-pgid, signal) };
    if rc == 0 {
        return Ok(());
    }
    let err = std::io::Error::last_os_error();
    if err.raw_os_error() == Some(libc::ESRCH) {
        return Ok(());
    }
    Err(err)
}
