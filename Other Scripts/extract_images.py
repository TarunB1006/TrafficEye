# script to extract images from a video at a set frame interval

import cv2
import os

# Function to extract frames at a reduced frame rate
def extract_frames(video_path, output_folder, frame_skip):
    # Create the output directory if it doesn't exist
    vid_path = video_path.strip('videos\\')
    vid_path = vid_path.strip('.mp4')
    print(vid_path)
    print(output_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    saved_frame_count = 0
    success = True

    

    while success:
        # Read a frame
        success, frame = cap.read()

        if success:
            # Save every nth frame
            if frame_count % frame_skip == 0:
                frame_filename = os.path.join(output_folder, f"{vid_path}_frame_{saved_frame_count:05d}.jpg")
                cv2.imwrite(frame_filename, frame)
                saved_frame_count += 1

            frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {saved_frame_count} frames to {output_folder}")

# Example usage

vid_path_input = input("Enter video relative path: ")

video_path = vid_path_input
output_folder = input("enter destination image folder: ")
frame_skip = 50  # Change this value to skip frames

extract_frames(video_path, output_folder, frame_skip)
