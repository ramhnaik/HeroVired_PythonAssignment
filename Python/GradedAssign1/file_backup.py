"""
Python program to back up directory
"""
import sys
import os
import shutil
from datetime import datetime


def backup_directory(source_dir, dest_dir):
    """
    To copy all files from the source directory to the destination directory.

    Parameters:-
        source_dir : str
                Source directory path provided by user.
        dest_dir : str
                Destination directory path provided by user.

    Return: Nil
    """

    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
            print(f"Created destination directory '{dest_dir}'.")
        except Exception as error:
            print(f"Error: Could not create destination directory '{dest_dir}'. {error}")
            return

    # Copy files from source to destination
    for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file)
        if os.path.isfile(source_file):
            destination_file = os.path.join(dest_dir, file)

            if os.path.exists(destination_file):
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                name, ext = os.path.splitext(file)
                destination_file = os.path.join(dest_dir, f"{name}_{timestamp}{ext}")

            try:
                shutil.copy2(source_file, destination_file)
                print(f"Copied '{source_file}' to '{destination_file}'.")
            except Exception as error:
                print(f"Error during backup: {error}")

    print("Backup completed successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file_backup.py <source_directory> <destination_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_directory(source_directory, destination_directory)
