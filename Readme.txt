# Worker Activity Detection using MediaPipe & OpenCV

This project monitors and logs a worker's activity status ("Working" or "Idle") using video input. It uses pose/face landmarks to infer activity levels in real-time.

### Key Features
- Detects if the subject is actively moving or idle
- Uses **OpenCV and Mediapipe for motion + pose detection**(built-in, no need to upload seperate model file)
- Logs timestamps and status to a CSV file (`worker_activity_log.csv`)
- Designed considering **a single individual** (e.g., corporate/remote employee)
- The system uses MediaPipe Pose for detecting upper-body movements: Detects "Working" status during virtual calls via mouth movements, even without full-body motion
- Windows-compatible auto-start via `.bat` file (not systemd)

---

## Tech Stack
- Python 3.9.8
- OpenCV
- MediaPipe
- Conda virtual environment
- CSV file logging
- Tested on **Windows OS**

---

## Auto Start (Windows)
Instead of using `systemd` (used on Linux), i created a **`.bat` file** that:
- Activates the Conda environment
- Launches the script automatically

To make it run on startup:
1. Place the `start_worker_activity.bat` in this path:  
   `C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
2. This will auto-run the script every time the system starts.

---

## Files Included
- `worker_activity_system.py` – Main detection script
- `start_worker_activity.bat` – Easy launcher with environment activation
- `worker_activity_log.csv` – Output log file (auto-generated)
- `instructions.txt` – Setup & run guide
- `Readme` - info about developed cv sytem project 

## 📸 Sample Use
Run a webcam or video file, and it will log activity status based on motion + pose.

## License
None
