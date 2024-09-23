import os
import shutil

def combine_folders(folder1, folder2, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for root, dirs, files in os.walk(folder1):
        relative_path = os.path.relpath(root, folder1)
        dest_path = os.path.join(destination_folder, relative_path)
        
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)
            if not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_file)
    
    for root, dirs, files in os.walk(folder2):
        relative_path = os.path.relpath(root, folder2)
        dest_path = os.path.join(destination_folder, relative_path)
        
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)
            if not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_file)
            else:
                base, extension = os.path.splitext(file)
                counter = 1
                new_dest_file = os.path.join(dest_path, f"{base}_{counter}{extension}")
                while os.path.exists(new_dest_file):
                    counter += 1
                    new_dest_file = os.path.join(dest_path, f"{base}_{counter}{extension}")
                shutil.copy2(src_file, new_dest_file)


folder1 = 'v9_data/v9_data_combined'
folder2 = 'v9_data/half'
destination_folder = 'v9_data/v9_data_full'

combine_folders(folder1, folder2, destination_folder)
