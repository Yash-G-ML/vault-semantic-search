import shutil
import os

def move_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Check if the destination folder exists; if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of files in the source folder
    files = os.listdir(source_folder)

    # Move each file to the destination folder
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' from {source_folder} to {destination_folder}")
        except Exception as e:
            print(f"Error moving '{file}': {e}")
            
    return destination_folder