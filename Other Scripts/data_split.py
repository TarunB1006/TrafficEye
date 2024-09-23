# script to split data into train, validation, and test sets

import os
import shutil
import random
from glob import glob

# Paths
images_folder = r"C:\Python Projects\police_hackathon\AutoData v1\SBI_FIX_1"
labels_folder = r"C:\Python Projects\police_hackathon\AutoData v1\SBI_FIX_1_labels"

train_ratio = 0.8
valid_ratio = 0.10
test_ratio = 0.10

# Get all image file paths
image_files = glob(os.path.join(images_folder, '*.jpg'))  # Adjust if not .jpg

# Shuffle the files
random.shuffle(image_files)

# Split the data
train_split = int(train_ratio * len(image_files))
valid_split = int(valid_ratio * len(image_files)) + train_split

train_files = image_files[:train_split]
valid_files = image_files[train_split:valid_split]
test_files = image_files[valid_split:]

# Function to move files
def move_files(files, set_name):
    os.makedirs(f'{set_name}/images/', exist_ok=True)
    os.makedirs(f'{set_name}/labels/', exist_ok=True)

    for file in files:
        # Move the image
        shutil.copy(file, f'{set_name}/images/')

        # Check if the corresponding label exists
        base_name = os.path.splitext(os.path.basename(file))[0]
        label_file = os.path.join(labels_folder, base_name + '.txt')

        if os.path.exists(label_file):
            shutil.copy(label_file, f'{set_name}/labels/')

# Move files to respective folders
move_files(train_files, 'train')
move_files(valid_files, 'val')
move_files(test_files, 'test')

print("Data split completed!")
