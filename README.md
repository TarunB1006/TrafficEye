# 🚦 TrafficEye

## [The Bengaluru Mobility Challenge, 2024](https://ieee-dataport.org/competitions/bengaluru-mobility-challenge-2024)

### 🏆 Team "GetFined"

> **Special Recognition Award** recipient for Phase 2 of the hackathon

**Team Members:**  
Sundarakrishnan N, Sohan Varier, Tarun Bhupathi, Manaswini SK  
*RV College of Engineering*

---

### 📚 Resources

- **Implementation Report:** [View Report](https://drive.google.com/drive/folders/1SgSUCLQtGbJ0AU8lXPIoKuy1wrObCNiG)
- **Event Details:** [Learn More](https://dataforpublicgood.org.in/bengaluru-mobility-challenge-2024/)

---

## 🐳 Docker

A Dockerfile has been created to install necessary libraries including CUDA for the model to be able to use GPUs. The docker file can be built and run in a simple way.

### Commands

**Build:**
```bash
docker build -t username/imagename:version
```

**Push:**
```bash
docker push username/imagename:version
```

**Run:**
```bash
docker run --rm --runtime=nvidia --gpus all -v 'YOUR STORAGE MOUNT':/app/data username/imagename:version python3 app.py input.json <output-folder-directory>
```

The run command takes the input and output json file to read, process and save the results in. Build creates the docker container and push command is used to push it to the docker repository so that anyone can pull the image and run the same.

---

## 📁 Scripts and Files

### Program Scripts

This folder contains all the files needed to run the pipeline:

1. **`app.py`**  
   The main driver code that has to be run. Takes an input JSON file and output file directory as CLI arguments that provide the video paths and the path to the final output folder, where the images and matrices will be stored after processing.

2. **`best.pt`**  
   The most important file, our trained YOLOv8 model to detect the 7 classes of vehicles.

3. **`deep_sort_realtime` folder**  
   The DeepSort-realtime library that we downloaded locally, as we had to make minor changes to the source code to suit our needs.
   - In `tracker.py`, modified the code to return the classes of the detections as well, along with the unique ID.

### Usage

Only `app.py` is supposed to be run, the other files cannot run on their own.

**Command to run:**
```bash
python3 app.py input.json <output-folder-directory>
```

`<output-folder-directory>` refers to the folder under which the final matrices and images are stored.

**Format for `input.json`:**
```json
{
    "Cam1": "/app/data/Cam_1_vid.mp4",
    "Cam2": "/app/data/Cam_2_vid.mp4"
}
```

---

### Other Scripts

These are some other scripts used to ease the process of training and development but is not needed to run the framework:

1. **`extract_images.py`**  
   We used this script to extract images from the video downloaded from the dataset every *n* frames which we can set based on the number of images required.

2. **`auto_annotate.py`**  
   After making a basic model, we ran the extracted images through the model to annotate the images for us, and we would verify/edit the annotations. This script automated the annotation process and saved us a lot of time.

3. **`data_split.py`**  
   A simple script to split the images dataset into training, testing and validation sets.

4. **`stream.py`**  
   This code lets us view the YOLO model in action on a live video. It shows us the predictions being made in real-time in the video.

5. **`data.yaml`**  
   This file is used to specify dataset location during training, and holds the list of classes.

---

## 📦 Requirements

| Package | Version | Description |
|---------|---------|-------------|
| **opencv_python_headless** | 4.10.0.84 | Used to read the video files and display them if needed |
| **ultralytics** | 8.2.58 | The library that contains YOLOv8, the model we used for vehicle detection and counting |
| **pandas** | 1.5.3 | The basic data structure used throughout the project, pandas dataframes |
| **Pillow** | 10.4.0 | Python's Image Library (PIL) that is used to view and manipulate images |
| **torchreid** | 0.2.5 | A re-id library used by DeepSort. This is the library used in our re-identification model |

---

## 🔧 Open-Source Material

- **YOLOv8** by *Ultralytics*  
  An open source, real-time object detection and image segmentation model.

- **labelimg**  
  An annotation tool that provides features to draw and edit bounding boxes in the format required by YOLOv8.

- **DeepSort**  
  A library that contains pre-trained re-identification models that we can make use of. It makes use of the detections done by the YOLO model, and checks whether any of those are re-appearing later.

---

## 💻 System Requirements

| Component | Specification |
|-----------|---------------|
| **CPU** | Core i5 |
| **GPU** | NVIDIA GTX 1650 |
| **RAM** | 8 GB |
| **Storage** | 10 GB |
| **GPU Memory** | ~1 GB (for realtime inference) |

---
