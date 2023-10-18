import os

# Define the directory containing your images
image_directory = '/home/rajat/Desktop/hate_train'

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

# Create a text file to store the paths
output_file_path = '/home/rajat/Desktop/IVP/hateMemesList.txt.train'

# Open the file in write mode
with open(output_file_path, 'w') as output_file:
    # Write each image path to the file
    for image_file in image_files:
        image_path = image_file
        output_file.write(image_path + '\n')

print(f'Paths of {len(image_files)} images written to {output_file_path}.')
