
import os
import shutil

# Folder containing the files
source_folder = "source_folder"

# Folder where we want to move the files
destination_folder = "destination_folder"

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get all files from the source folder
files = os.listdir(source_folder)

# Check each file
for file in files:

    # Check if the file ends with .jpg
    if file.lower().endswith(".jpg"):

        # Create the complete path of the source file
        source_path = os.path.join(source_folder, file)

        # Create the complete path of the destination file
        destination_path = os.path.join(destination_folder, file)

        # Move the file
        shutil.move(source_path, destination_path)

        print(file, "moved successfully!")

print("All JPG files have been moved.")
