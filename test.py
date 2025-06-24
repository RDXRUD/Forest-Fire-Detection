
from ultralytics import YOLO
import cv2

# Load a pre-trained YOLOv10n model
model = YOLO("yolo/new_dataset/yolov10/SGD_10s/weights/best.pt")

# Open the video file or capture from a camera (use "0" for webcam)
video_path = "/content/Forest fires reach record levels across globe l ABC News.mp4"  # replace with your video file path
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Loop through frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if there are no more frames

    # Perform object detection on the frame
    results = model(frame)

    # Draw results on the frame
    annotated_frame = results[0].plot()  # Use plot() for annotated output

    # Display the annotated frame
    cv2.imshow("YOLOv10s Object Detection", annotated_frame)

    # Press 'q' to exit the video display
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()