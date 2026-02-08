<div align="center">

# 🚦 TrafficEye
### Intelligent Vehicle Detection & Tracking System

[![Challenge](https://img.shields.io/badge/Bengaluru%20Mobility-Challenge%202024-blue?style=for-the-badge)](https://ieee-dataport.org/competitions/bengaluru-mobility-challenge-2024)
[![Award](https://img.shields.io/badge/🏆-Special%20Recognition%20Award-gold?style=for-the-badge)](https://dataforpublicgood.org.in/bengaluru-mobility-challenge-2024/)
[![Team](https://img.shields.io/badge/Team-GetFined-green?style=for-the-badge)](#)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat&logo=nvidia&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=flat&logo=yolo&logoColor=black)

</div>

---

## 🏆 Achievement

> **🎉 Special Recognition Award** - Phase 2 of the Bengaluru Mobility Challenge 2024

<div align="center">

### 👥 Team "GetFined"

| Member | Role |
|:------:|:----:|
| 🧑‍💻 Sundarakrishnan N | Developer |
| 🧑‍💻 Sohan Varier | Developer |
| 🧑‍💻 Tarun Bhupathi | Developer |
| 🧑‍💻 Manaswini SK | Developer |

**🏛️ RV College of Engineering**

</div>

---

## 📚 Documentation & Resources

<table>
<tr>
<td align="center" width="50%">

### 📄 Implementation Report
[![Report](https://img.shields.io/badge/View-Report-blue?style=for-the-badge&logo=google-drive)](https://drive.google.com/drive/folders/1SgSUCLQtGbJ0AU8lXPIoKuy1wrObCNiG)

</td>
<td align="center" width="50%">

### 🌐 Event Details
[![Event](https://img.shields.io/badge/Learn-More-orange?style=for-the-badge&logo=safari)](https://dataforpublicgood.org.in/bengaluru-mobility-challenge-2024/)

</td>
</tr>
</table>

---

## 🐳 Docker Deployment

<div align="center">

![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-Support-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

</div>

A Dockerfile has been created to install necessary libraries including CUDA for the model to be able to use GPUs. The docker file can be built and run in a simple way.

### 🔧 Commands

<table>
<tr>
<td width="20%"><b>🏗️ Build</b></td>
<td width="80%">

```bash
docker build -t username/imagename:version
```

</td>
</tr>
<tr>
<td width="20%"><b>📤 Push</b></td>
<td width="80%">

```bash
docker push username/imagename:version
```

</td>
</tr>
<tr>
<td width="20%"><b>▶️ Run</b></td>
<td width="80%">

```bash
docker run --rm --runtime=nvidia --gpus all -v 'YOUR STORAGE MOUNT':/app/data username/imagename:version python3 app.py input.json <output-folder-directory>
```

</td>
</tr>
</table>

> 💡 **Note:** The run command takes the input and output json file to read, process and save the results in. Build creates the docker container and push command is used to push it to the docker repository so that anyone can pull the image and run the same.

---

## 📁 Project Structure

### 🎯 Program Scripts

<div align="center">

| File | Description |
|:----:|:------------|
| 🐍 **`app.py`** | The main driver code that has to be run. Takes an input JSON file and output file directory as CLI arguments that provide the video paths and the path to the final output folder, where the images and matrices will be stored after processing. |
| 🎯 **`best.pt`** | The most important file, our trained YOLOv8 model to detect the 7 classes of vehicles. |
| 📂 **`deep_sort_realtime/`** | The DeepSort-realtime library that we downloaded locally, as we had to make minor changes to the source code to suit our needs.<br/>• In `tracker.py`, modified the code to return the classes of the detections as well, along with the unique ID. |

</div>

### 🚀 Quick Start

> ⚠️ **Important:** Only `app.py` is supposed to be run, the other files cannot run on their own.

**▶��� Command to run:**
```bash
python3 app.py input.json <output-folder-directory>
```

**📝 Input Configuration:**

`<output-folder-directory>` refers to the folder under which the final matrices and images are stored.

**Format for `input.json`:**
```json
{
    "Cam1": "/app/data/Cam_1_vid.mp4",
    "Cam2": "/app/data/Cam_2_vid.mp4"
}
```

---

### 🛠️ Utility Scripts

<details>
<summary><b>Click to expand utility scripts</b></summary>

These are some other scripts used to ease the process of training and development but is not needed to run the framework:

| Script | Purpose |
|:------:|:--------|
| 🖼️ **`extract_images.py`** | We used this script to extract images from the video downloaded from the dataset every *n* frames which we can set based on the number of images required. |
| 🏷️ **`auto_annotate.py`** | After making a basic model, we ran the extracted images through the model to annotate the images for us, and we would verify/edit the annotations. This script automated the annotation process and saved us a lot of time. |
| ✂️ **`data_split.py`** | A simple script to split the images dataset into training, testing and validation sets. |
| 🎥 **`stream.py`** | This code lets us view the YOLO model in action on a live video. It shows us the predictions being made in real-time in the video. |
| 📋 **`data.yaml`** | This file is used to specify dataset location during training, and holds the list of classes. |

</details>

---

## 📦 Dependencies

<div align="center">

### Required Python Packages

| Package | Version | Purpose | Badge |
|:-------:|:-------:|:--------|:-----:|
| **opencv_python_headless** | `4.10.0.84` | Used to read the video files and display them if needed | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white) |
| **ultralytics** | `8.2.58` | The library that contains YOLOv8, the model we used for vehicle detection and counting | ![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=flat) |
| **pandas** | `1.5.3` | The basic data structure used throughout the project, pandas dataframes | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) |
| **Pillow** | `10.4.0` | Python's Image Library (PIL) that is used to view and manipulate images | ![Pillow](https://img.shields.io/badge/Pillow-FFD43B?style=flat) |
| **torchreid** | `0.2.5` | A re-id library used by DeepSort. This is the library used in our re-identification model | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white) |

</div>

---

## 🔧 Open-Source Technologies

<div align="center">

<table>
<tr>
<td align="center" width="33%">

### 🎯 YOLOv8
**by *Ultralytics***

![YOLO](https://img.shields.io/badge/YOLOv8-Detection-00FFFF?style=for-the-badge)

An open source, real-time object detection and image segmentation model.

</td>
<td align="center" width="33%">

### 🏷️ LabelImg
**Annotation Tool**

![LabelImg](https://img.shields.io/badge/LabelImg-Annotation-green?style=for-the-badge)

An annotation tool that provides features to draw and edit bounding boxes in the format required by YOLOv8.

</td>
<td align="center" width="33%">

### 🔍 DeepSort
**Tracking Library**

![DeepSort](https://img.shields.io/badge/DeepSort-Tracking-red?style=for-the-badge)

A library that contains pre-trained re-identification models that we can make use of. It makes use of the detections done by the YOLO model, and checks whether any of those are re-appearing later.

</td>
</tr>
</table>

</div>

---

## 💻 System Requirements

<div align="center">

### 🖥️ Minimum Hardware Specifications

| Component | Specification | Icon |
|:---------:|:-------------:|:----:|
| **Processor** | Intel Core i5 | 🔲 |
| **Graphics** | NVIDIA GTX 1650 | 🎮 |
| **Memory** | 8 GB RAM | 🧠 |
| **Storage** | 10 GB SATA | 💾 |
| **VRAM Usage** | ~1 GB (realtime inference) | ⚡ |

</div>

---

<div align="center">

### 🌟 Built with passion by Team GetFined 🌟

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Powered%20by-AI-orange?style=for-the-badge)

**📧 Questions? Feel free to reach out!**

---

⭐ **If you find this project helpful, please consider giving it a star!** ⭐

</div>
