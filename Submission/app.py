import datetime
from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort
import os
import json
import sys

# Load the JSON file containing video paths from the command-line argument
if len(sys.argv) != 3:
    print("Usage: python script.py <path_to_json>")
    sys.exit(1)

json_file_path = sys.argv[1]
output_file_path=sys.argv[2]

# Read the JSON file
with open(json_file_path, 'r') as f:
    video_locations = json.load(f)
video_paths = list(video_locations.values())

vehicle_classes = ["Car", "Bus", "Truck", "Three-Wheeler", "Two-Wheeler", "LCV", "Bicycle"]

output_dir = "Images"
os.makedirs(os.path.join(output_file_path,output_dir), exist_ok=True)
for vehicle_class in vehicle_classes:
    class_dir = os.path.join(os.path.join(output_file_path,output_dir), vehicle_class)
    os.makedirs(class_dir, exist_ok=True)
matrices_dir = "Matrices"
os.makedirs(os.path.join(output_file_path,matrices_dir), exist_ok=True)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


# Load the pre-trained YOLOv8n model
model = YOLO(r"best.pt")

# Initialize the tracker
tracker = DeepSort(max_age=15*60*50*4,n_init=10,embedder='torchreid')

# Initialize a list to store sets of (ID, predicted class) tuples for each video
ids_list = [set() for _ in range(len(video_paths))]

# Process each video
for video_idx, video_path in enumerate(video_paths):
    video_cap = cv2.VideoCapture(video_path)
    
    # Dictionary to map detection IDs to their predicted class
    frame_count = 0
    saved_ids_per_cam = []
    while True:
        start = datetime.datetime.now()

        ret, frame = video_cap.read()
        if not ret:
            break
        frame_count += 1
        # Run the YOLO model on the frame
        detections = model(frame, conf=0.5)[0]
        dup_frame=frame.copy()
        # Initialize the list of bounding boxes and confidences
        results = []

        # Map detection indices to their class IDs
        for i, data in enumerate(detections.boxes.data.tolist()):
            confidence = data[4]
            xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            class_id = int(data[5])
            results.append([[xmin, ymin, xmax - xmin, ymax - ymin], confidence, class_id])

        # Update the tracker with the new detections
        tracks, present_ids = tracker.update_tracks(results, frame=frame)
        # print('Present ids: ', present_ids)
        # Add (ID, predicted class) tuples to the set corresponding to the current video
        
        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            # Find the detection index corresponding to the track ID
            # Here, you should map track_id to detection indices appropriately
            actual_ids = []
            for dets in present_ids:
                ids_list[video_idx].add((dets[0], vehicle_classes[dets[1]]))
                actual_ids.append(dets[0])
           
            # Draw the bounding box and track ID
            if track_id in actual_ids:
                new_frame=dup_frame.copy()
                ltrb = track.to_ltrb(orig=True)
                xmin, ymin, xmax, ymax = int(ltrb[0]), int(ltrb[1]), int(ltrb[2]), int(ltrb[3])
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), GREEN, 2)
                cv2.rectangle(frame, (xmin, ymin - 20), (xmin + 20, ymin), GREEN, -1)
                cv2.putText(frame, str(track_id), (xmin + 5, ymin - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 2)
                if track_id in saved_ids_per_cam:
                    continue  
                          # The class index

                # Iterate through the tuples in ids_list[video_idx] to find the match
                class_name=""
                for detection in ids_list[video_idx]:
                    if detection[0] == track_id:
                        class_name = detection[1]
                        break
                
                annotation_text = f"{class_name}_Cam{video_idx + 1}_Frame{frame_count}_ID{track_id}"
                cv2.rectangle(new_frame, (xmin, ymin), (xmax, ymax), GREEN, 2)
                cv2.rectangle(new_frame, (xmin, ymin - 20), (xmin + 20, ymin), GREEN, -1)
                cv2.putText(new_frame, annotation_text, (xmin + 5, ymin - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, WHITE, 2)
                
                # Save the snapshot in the appropriate class subfolder
                snapshot_path = os.path.join(output_dir, class_name, f"{annotation_text}.jpg")
                cv2.imwrite(os.path.join(output_file_path,snapshot_path), new_frame)
                saved_ids_per_cam.append(track_id)
        # End time to compute the fps
        end = datetime.datetime.now()
        # Show the time it took to process 1 frame
        print(f"Time to process 1 frame: {(end - start).total_seconds() * 1000:.0f} milliseconds")
        # Calculate the frame per second and draw it on the frame
        fps = f"FPS: {1 / (end - start).total_seconds():.2f}"
        cv2.putText(frame, fps, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 8)



    video_cap.release()



# Print the list of sets of (ID, predicted class) tuples for each video
for idx, ids in enumerate(ids_list):
    print(f"IDs and classes for video {idx + 1}: {ids}")

repeats = dict()

for i in range(0, len(video_paths)-1):
    for j in range(i+1, len(video_paths)):
        repeats[i+1,j+1] = ids_list[i].intersection(ids_list[j])
        

print("repeats: ", repeats)

final = {x: [[0 for i in range(len(video_paths))] for j in range(len(video_paths))] for x in vehicle_classes}

for key in repeats:
    for val in repeats[key]:
        final[val[1]][key[0]-1][key[1]-1] += 1




print("final: ", final)
for vehicle_class in vehicle_classes:
    matrix_file_path = os.path.join(os.path.join(output_file_path,matrices_dir), f"{vehicle_class}.json")
    with open(matrix_file_path, 'w') as json_file:
        json.dump(final[vehicle_class], json_file, indent=4)

print("final matrices saved in matrices folder")