import os
import random
import shutil

# Define the paths for your source and target folders
source_folder = '/home/rajat/Desktop/HateFul_Memes_Dataset/data/label_1/img'
target_folder1 = '/home/rajat/Desktop/hate_train'
target_folder2 = '/home/rajat/Desktop/hate_validation'

random.seed(42) 

# Get a list of all the files in the source folder
files = os.listdir(source_folder)

# Calculate the number of files for each category
total_files = len(files)
split_point = int(0.85 * total_files)

# Shuffle the list of files
random.shuffle(files)

# Copy the files to the target folders
for i, file in enumerate(files):
    source_path = os.path.join(source_folder, file)
    if i < split_point:
        target_path = os.path.join(target_folder1, file)
    else:
        target_path = os.path.join(target_folder2, file)
    shutil.copy(source_path, target_path)
