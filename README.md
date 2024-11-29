# DIP Course Object Tracking Algorithm

This repository contains the implementation of various object tracking algorithms as part of the DIP (Digital Image Processing) course project. The main focus is on using OpenCV to implement and compare different tracking algorithms, including CSRT.

Experimented Video and PPTX can be found here - https://drive.google.com/drive/folders/10o4gs3xFm7XHcAKdT3nS-ywD2uGspcPE?usp=sharing
---

## Author Information

- **Name**: Meliboev Shukurullo
- **Student ID**: 12225261
- **University**: Inha University
- **Course**: Digital Image Processing Design

---

## Features

- Implementation of multiple tracking algorithms:
  - CSRT
  - MIL
  - KCF
  - BOOSTING
  - TLD
  - MEDIANFLOW
  - MOSSE
- Real-time FPS display.
- Supports custom ROI selection.
- Videos and results are saved and shared via Google Drive.

---

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/shukurullo2004/DIP_course_object_tracking_algorithm.git
   cd DIP_course_object_tracking_algorithm
2.Create a virtual environment and activate it:
```
  python -m venv shenv
  source shenv/bin/activate  # Linux/MacOS
  shenv\Scripts\activate     # Windows
```
3.Install the required dependencies:
```
  pip install -r requirements.txt
```
4.Usage
Run the Tracking Script
To run the main tracking script:
```
  python tracking.py
```
5.Supported Features
Select the region of interest (ROI) by dragging over the video frame.
Track the object in real-time.
Displays FPS for the selected tracking algorithm.
Tracking Algorithms
Description
This project implements and compares the following tracking algorithms:

CSRT: High accuracy, suitable for complex object motion and dynamic backgrounds.
KCF: Fast and efficient for simple tracking tasks.
MIL: Handles partial occlusion but less robust for fast motion.
BOOSTING: Lightweight, legacy implementation.
MEDIANFLOW: Accurate for steady motion but fails with occlusion.
MOSSE: Extremely fast but less accurate.
TLD: Adapts to changes in object appearance but prone to false positives.
How to Use:
Modify the TRACKER_TYPES list in tracking.py to select the desired tracking algorithm.
6.Repository Structure
```
  DIP_course_object_tracking_algorithm/
  ├── tracking.py          # Main tracking script
  ├── csrt_tracking.py     # Specific implementation for CSRT
  ├── requirements.txt     # Python dependencies
  ├── output/              # Folder for saving local output videos
  └── README.md            # Project documentation
```
