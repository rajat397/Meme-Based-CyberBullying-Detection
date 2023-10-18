# Define the input and output file paths
input_file = '/home/rajat/Desktop/IVP/redditMemesList.txt.train'
output_file = '/home/rajat/Desktop/IVP/non_hateMemesList.txt.train'

# Read lines from the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Filter out lines with .ocr extension
filtered_lines = [line.strip() for line in lines if '.ocr' not in line]

# Write the filtered lines to the output file
cnt = len(filtered_lines)  # Count the number of filtered lines
with open(output_file, 'w') as file:
    file.write('\n'.join(filtered_lines))

print(f'Filtered {cnt} filenames saved to {output_file}')

