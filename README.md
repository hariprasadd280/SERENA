# PROJECT SERENA (Sentient Emotional Response and Engagement Nurse with Assistance)

SERENA is an AI-powered emotional support and physical assistance robot designed for elderly care in home environments[cite: 2]. Developed at Government Engineering College, Barton Hill (APJ Abdul Kalam Technological University)[cite: 2], SERENA integrates computer vision, speech processing, and smart hardware actuation to enhance well-being and safe daily living[cite: 2].

---

## Key Capabilities

* **Facial Emotion Recognition (FER):** Real-time CNN model classifying 7 facial emotional states.
* **Fall Detection & Posture Monitoring:** MediaPipe pose estimation tracking landmark vertical shifts.
* **Automated Pill Dispenser (SPD):** ESP32-driven stepper and servo actuation for scheduled medication.
* **Cloud Synchronization & Alerts:** Integrated Firebase database notifying caregiver app during emergencies.

---

## Hardware Architecture

| Component | Specifications |
| :--- | :--- |
| **Main Processing Unit** | NVIDIA Jetson Nano |
| **Microcontroller** | ESP32 (Wi-Fi / Bluetooth) |
| **Dimensions** | $34 \times 30 \times 63 \text{ cm}$ |
| **Locomotion** | Differential DC Motor Drive (L298N) |

---

## Project Structure

```text
├── app/
│   └── main.py              # Vision & Fall Detection Pipeline
├── firmware/
│   └── spd_controller.ino   # ESP32 Smart Pill Dispenser Firmware
├── models/
│   └── emotion_model.json   # CNN Emotion Architecture Definition
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
└── README.md
