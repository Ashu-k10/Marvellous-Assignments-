# Write a program that monitorst the size of a specified file every 30 seconds.

# Write the following details into:
# FileSizeLog.txt
#   •File path
#   •File Size in bytes
#   •Date & time
# Handles the situation where the file does not exists

import os
import schedule
import time
import datetime

def FileSizeMonitor(FilePath):

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("FileSizeLog.txt", "a") as logfile:

        logfile.write("-" * 50 + "\n")

        if os.path.exists(FilePath):

            filesize = os.path.getsize(FilePath)

            logfile.write(f"File Path : {FilePath}\n")
            logfile.write(f"File Size : {filesize} bytes\n")
            logfile.write(f"Date & Time : {current_time}\n")

            print(f"Checked : {filesize} bytes")

        else:

            logfile.write(f"File Path : {FilePath}\n")
            logfile.write("Status : File does not exist.\n")
            logfile.write(f"Date & Time : {current_time}\n")

            print("File does not exist.")

def main():

    FilePath = input("Enter File Path : ")

    # Schedule the monitoring every 30 seconds
    schedule.every(30).seconds.do(FileSizeMonitor, FilePath)

    print("File Monitoring Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


