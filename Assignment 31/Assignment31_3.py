# Write a program that scans a specified directory every minutes
# The task should display:
#                • Directory name
#                • Number of files
#                • Number of subdirectories
#                • Date & Time of scanning 
# Use the os module
# Example output :
# Directory Scanned : E:/Data
# Total Files : 15
# Total Subdirectories : 4

import os
import time
import datetime 

def DirectoryScanner(path):
    if not os.path.exists(path):
        print("Directory does not exist.")
        return

    files = 0
    folders = 0

    # Scan the directory
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            files += 1
        elif os.path.isdir(full_path):
            folders += 1

    print("\n-------------------------------")
    print("Directory Scanned :", path)
    print("Total Files       :", files)
    print("Total Subdirectories :", folders)
    print("Scan Time         :", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-------------------------------")

def main():
    DirectoryPath = input("Enter directory path: ")

    while True:
        DirectoryScanner(DirectoryPath)
        print("Waiting for 1 minute...\n")
        time.sleep(60)      # Wait for 60 seconds

if __name__ == "__main__":
    main()