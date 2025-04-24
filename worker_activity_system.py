##mediapipe libaray works fir with python version 3.8 to 3.10
##Python 3.9.21

import cv2
import numpy as np
import mediapipe as mp
import csv
from datetime import datetime

mp_pose = mp.solutions.pose #MediaPipe Pose Estimation
pose = mp_pose.Pose()

fgbg = cv2.createBackgroundSubtractorMOG2()   # Background Subtraction

cap = cv2.VideoCapture(0)  # Video capture from webcam

# Function to overwrite csv for every fresh input)
def init_log_file():
    with open('worker_activity_log.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Activity"])

# Function to log activity status
def log_activity(status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('worker_activity_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, status])

# Check if capture source is valid
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize the log file once
init_log_file()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized = cv2.resize(frame, (640, 640))
    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

    # Pose detection
    results = pose.process(frame_rgb)

    # Motion detection
    fgmask = fgbg.apply(frame_resized)
    motion_pixels = np.count_nonzero(fgmask)

    if motion_pixels > 4000:    # Motion threshold
        activity_status = "Working"
    else:
        activity_status = "Idle"

    log_activity(activity_status)

    # Draw pose landmarks
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            frame_resized,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
            connection_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=2)
        )

    # Display activity status on frame
    cv2.putText(frame_resized, f"Status: {activity_status}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Worker Activity Detection", frame_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
