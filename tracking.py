import cv2
import time
import os
import random

# List of tracker types
TRACKER_TYPES = [
    "BOOSTING",
    "MIL",
    "KCF",
    "TLD",
    "MEDIANFLOW",
    "GOTURN",
    "CSRT",
    "MOSSE"
]

# Define a function to generate a random color for each tracker
def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Define colors for each tracker type
TRACKER_COLORS = {
    "BOOSTING": (0, 255, 0),       # Green
    "MIL": (255, 165, 0),         # Red
    "KCF": (255, 0, 0),            # Blue
    "TLD": (255, 255, 0),          # Yellow
    "MEDIANFLOW": (0, 200, 55),   # Cyan
    "GOTURN": (255, 0, 255),       # Magenta
    "CSRT": (0, 0, 255),         # Orange
    "MOSSE": (128, 0, 128),        # Purple
}

def create_tracker(tracker_type):
    if tracker_type == "BOOSTING":
        return cv2.legacy.TrackerBoosting_create()
    elif tracker_type == "MIL":
        return cv2.legacy.TrackerMIL_create()
    elif tracker_type == "KCF":
        return cv2.legacy.TrackerKCF_create()
    elif tracker_type == "TLD":
        return cv2.legacy.TrackerTLD_create()
    elif tracker_type == "MEDIANFLOW":
        return cv2.legacy.TrackerMedianFlow_create()
    elif tracker_type == "CSRT":
        return cv2.legacy.TrackerCSRT_create()
    elif tracker_type == "MOSSE":
        return cv2.legacy.TrackerMOSSE_create()
    else:
        print(f"Invalid tracker type: {tracker_type}")
        return None

def main():
    # Load video
    video = cv2.VideoCapture(0)  # Use 0 for webcam or replace with video file path
    ret, frame = video.read()
    if not ret:
        print("Failed to load video")
        return
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    output_file = "output.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
    out = cv2.VideoWriter(output_file, fourcc, 30, (frame_width, frame_height))  # 30 FPS

    # Select ROI
    bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
    if bbox == (0, 0, 0, 0):
        print("No ROI selected. Exiting.")
        return

    # Initialize all trackers
    trackers = {}
    for tracker_type in TRACKER_TYPES:
        tracker = create_tracker(tracker_type)
        if tracker:
            tracker.init(frame, bbox)
            trackers[tracker_type] = tracker

    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame_results = []

        for tracker_type, tracker in trackers.items():
            start_time = time.time()

            # Update tracker
            success, bbox = tracker.update(frame)
            elapsed_time = time.time() - start_time

            # Calculate FPS for this tracker
            fps = 1 / elapsed_time

            if success:
                # Draw bounding box with color specific to tracker
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                color = TRACKER_COLORS.get(tracker_type, (255, 255, 255))  # Default to white if no color assigned
                cv2.rectangle(frame, p1, p2, color, 2, 1)

                # Add tracker result to frame display
                frame_results.append(f"{tracker_type}: FPS={fps:.2f}")
            else:
                frame_results.append(f"{tracker_type}: FAILED")

        # Display tracker metrics on the frame
        y_offset = 20
        for result in frame_results:
            tracker_type = result.split(":")[0]
            color = TRACKER_COLORS.get(tracker_type, (255, 255, 255))  # Default to white if no color assigned
            cv2.putText(frame, result, (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            y_offset += 20
        out.write(frame)
        cv2.imshow("Tracking Comparison", frame)

        # Break on ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
