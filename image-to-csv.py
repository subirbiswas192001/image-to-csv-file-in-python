import os
import pandas as pd

# Define the path to the root folder
root_folder = 'SB-FishDisease'  

# Initialize empty lists to store folder names, image filenames, and image paths
folder_names = []
image_filenames = []
image_paths = []

# Iterate through the subfolders in the root folder
for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    
    # Check if the item in the root folder is a directory (subfolder)
    if os.path.isdir(folder_path):
        # Iterate through the files in the subfolder
        for filename in os.listdir(folder_path):
            # Check if the file is an image (you can specify additional extensions)
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                folder_names.append(folder_name)
                image_filenames.append(filename)
                image_paths.append(os.path.join(folder_path, filename))

# Create a DataFrame to store the data
data = {'Folder Name': folder_names, 'Image Filename': image_filenames, 'Image Path': image_paths}
df = pd.DataFrame(data)

# Define the output CSV file path
output_csv = 'SB-Fish-Disease.csv'

# Save the DataFrame to a CSV file
df.to_csv(output_csv, index=False)

print(f"Image dataset information saved to {output_csv}")


