import os

def check_files_presence(file_list, folder_path, output_file):
    missing_files = []

    with open(file_list, 'r') as f:
        lines = f.readlines()

    for line in lines:
        filename = line.strip()

        if not os.path.exists(os.path.join(folder_path, filename)):
            missing_files.append(filename)

    with open(output_file, 'w') as f:
        if missing_files:
            f.write("The following files are missing:\n")
            for file in missing_files:
                f.write(f"{file}\n")
        else:
            f.write("All files are present in the specified folder.")

# Usage
file_list = "/home/rajat/Desktop/IVP/hateMemesList.txt.valid"  # Replace with your input file containing file names
folder_path = "/home/rajat/Desktop/hate-speech-detection/data/train_data"  # Replace with your folder path
output_file = "missing_files.txt"  # Output file to store missing files

print(file_list)
check_files_presence(file_list, folder_path, output_file)
