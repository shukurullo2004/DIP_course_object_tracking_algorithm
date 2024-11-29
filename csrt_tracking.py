import cv2
import time

def main():
    # Load video
    video = cv2.VideoCapture('/Users/shukurullomeliboyev2004/Desktop/university/DIP/cars.mp4')  # Use 0 for webcam or replace with a video file path
    ret, frame = video.read()
    if not ret:
        print("Failed to load video")
        return

    # Get frame width and height
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object for saving
    output_file = "csrt_output.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
    out = cv2.VideoWriter(output_file, fourcc, 30, (frame_width, frame_height))

    # Select ROI
    bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
    if bbox == (0, 0, 0, 0):
        print("No ROI selected. Exiting.")
        return

    # Initialize CSRT tracker
    tracker = cv2.legacy.TrackerCSRT_create()
    tracker.init(frame, bbox)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Start timer
        start_time = time.time()

        # Update tracker
        success, bbox = tracker.update(frame)

        # Calculate FPS
        fps = 1 / (time.time() - start_time)

        if success:
            # Draw bounding box
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)  # Blue bounding box
        else:
            cv2.putText(frame, "Tracking failure detected", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display tracker name
        cv2.putText(frame, "CSRT", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)  # White text

        # Display FPS in red color
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Write frame to the output video file
        out.write(frame)

        # Show the frame
        cv2.imshow("CSRT Tracking", frame)

        # Break on ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release resources
    video.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Video saved as {output_file}")

if __name__ == "__main__":
    main()
