# script to stream video and perform object detection for testing

import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO(r"best.pt")  

# Open the video file
cap = cv2.VideoCapture(r'videos\18th_Crs_Bus_Stop_FIX_2_time_2024-05-15T07_30_02_004.mp4')  

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Perform object detection
    results = model(frame)

    # Iterate over results and render each one
    for result in results:
        annotated_frame = result.plot()

    # Display the annotated frame
    cv2.imshow('YOLO Object Detection', annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
