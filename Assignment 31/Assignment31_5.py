# Write a program that accepts a directory name from the user and counts the numbers of files inside it every five minutes.
# Write the results into:

# DirectoryCountLog.txt
# Each entry should contain:
#      • Directory path
#      • Numbers of files
#      • Date and time

import os
import time
import datetime

def DirectoryCount(DirectoryPath):
    count = 0

    for item in os.listdir(DirectoryPath):
        if os.path.isfile(os.path.join(DirectoryPath, item)):
            count += 1

    return count

def WriteLog(DirectoryPath):
    filecount = DirectoryCount(DirectoryPath)

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("DirectoryCountLog.txt", "a") as logfile:
        logfile.write("-" * 50 + "\n")
        logfile.write(f"Directory Path : {DirectoryPath}\n")
        logfile.write(f"Number of Files : {filecount}\n")
        logfile.write(f"Date and Time : {current_time}\n")

    print("Log updated successfully.")

def main():
    DirectoryPath = input("Enter directory path : ")

    if not os.path.isdir(DirectoryPath):
        print("Invalid Directory")
        return

    print("Directory Monitoring Started...\n")

    while True:
        WriteLog(DirectoryPath)

        # Wait for 5 minutes (300 seconds)
        time.sleep(300)
    
if __name__ == "__main__":
    main()

