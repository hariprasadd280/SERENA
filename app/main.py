"""
PROJECT SERENA: Core Vision, Fall Detection, and Emotion Recognition Script
Run on NVIDIA Jetson Nano.
"""

import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose Estimation
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# EMOTION CATEGORIES
EMOTIONS = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

def detect_fall(landmarks, frame_height):
    """
    Monitors vertical shift of nose landmark to trigger emergency status.
    """
    nose_y = landmarks[mp_pose.PoseLandmark.NOSE.value].y * frame_height
    # Example threshold logic: if nose drops past 80% of frame height
    if nose_y > (0.80 * frame_height):
        return True
    return False

def main():
    cap = cv2.VideoCapture(0)
    
    print("[SERENA] Starting core system execution...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process Pose
        results = pose.process(rgb_frame)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            if detect_fall(landmarks, h):
                cv2.putText(frame, "ALERT: FALL DETECTED!", (30, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                # Firebase push alert logic goes here

        cv2.imshow("SERENA Core Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
