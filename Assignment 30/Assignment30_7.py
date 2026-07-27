# Write a python program that performs a file backup every hour.
# The Program should :
#    1. Accept the source file path
#    2. Accept the destination
#    3. Copy the source file to the destination directory
#    4. Add the current date and time to the backup filename
#    5. Write the backup operation details into:
#
#   backup_log.txt
#   example backup filename
#
#   Data 25_07_2026_16_30_00.txt
#   Example log entry:
#
#   Backup completed sucessfully at 25-07-2026 04:30:00 PM
#   Use the shutil module for file copying


import os
import shutil
import schedule
import time
from datetime import datetime

def BackupFile(SourceFile, DestinationFolder):

    if os.path.exists(SourceFile) == False:
        print("Source file not found")
        return

    filename = os.path.basename(SourceFile)

    name, ext = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    BackupName = f"{name}_{timestamp}{ext}"

    DestinationPath = os.path.join(DestinationFolder, BackupName)

    shutil.copy2(SourceFile, DestinationPath)

    logfile = open("backup_log.txt", "a")

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    logfile.write(f"Backup completed successfully at {current_time}\n")

    logfile.close()

    print("Backup Created Successfully")

def main():

    SourceFile = input("Enter source file path : ")
    DestinationFolder = input("Enter destination folder : ")

    schedule.every().hour.do(BackupFile, SourceFile, DestinationFolder)

    print("Backup Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


