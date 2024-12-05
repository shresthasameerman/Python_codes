import sys
import shutil
import os

def main():
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python backup_creator.py <filename>")
        return

    original_file = sys.argv[1]

    # Check if the specified file exists
    if not os.path.isfile(original_file):
        print(f"The file '{original_file}' does not exist.")
        return

    # Create a backup filename by appending '.bak' to the original filename
    backup_file = original_file + '.bak'

    # Use shutil to copy the original file to the backup file
    try:
        shutil.copyfile(original_file, backup_file)
        print(f"Backup of '{original_file}' created as '{backup_file}'.")
    except Exception as e:
        print(f"An error occurred while creating the backup: {e}")

if __name__ == "__main__":
    main()