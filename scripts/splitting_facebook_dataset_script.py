import json
import os
import shutil

# Define the paths
data_dir = '/home/rajat/Desktop/HateFul_Memes_Dataset/data'
json_file = os.path.join(data_dir, 'train.jsonl')
image_dir = data_dir

# Read the JSONL file
with open(json_file, 'r') as file:
    lines = file.readlines()

# Process each line in the JSONL file
for line in lines:
    data = json.loads(line)
    label = data['label']
    image_filename = data['img']

    # Source and destination paths
    source_path = os.path.join(image_dir, image_filename)
    output_dir = os.path.join(data_dir, f'label_{label}')

    if os.path.isfile(source_path):
        os.makedirs(output_dir, exist_ok=True)
        destination_path = os.path.join(output_dir, image_filename)

        try:
            # Copy the image
            shutil.copy(source_path, destination_path)

            # Remove the original
            os.remove(source_path)

        except Exception as e:
            print(f"Error occurred: {e}")
    else:
        print(f"File {source_path} does not exist. Skipping...")

print("Images separated based on labels.")
