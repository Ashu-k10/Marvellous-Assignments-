# Write a program that copiers all .txt files from one directory to another every ten minutes.
# The program should:
#    • Accept source and destination directories
#    • Validate both directories
#    • Copy only .txt files
#    • Maintain a log of copied files
#    • Avoid terminating if one file cannot be copied


import os
import shutil
import schedule
import time
import datetime

def CopyTextFiles(SourceDir, DestinationDir):

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("CopyLog.txt", "a") as logfile:

        logfile.write("\n" + "-" * 60 + "\n")
        logfile.write(f"Date & Time : {current_time}\n")

        for file in os.listdir(SourceDir):

            SourcePath = os.path.join(SourceDir, file)

            if os.path.isfile(SourcePath) and file.endswith(".txt"):

                try:
                    DestinationPath = os.path.join(DestinationDir, file)

                    shutil.copy2(SourcePath, DestinationPath)

                    logfile.write(f"Copied : {file}\n")
                    print(f"Copied : {file}")

                except Exception as e:

                    logfile.write(f"Failed : {file} --> {e}\n")
                    print(f"Failed : {file}")

def main():

    SourceDir = input("Enter Source Directory : ")
    DestinationDir = input("Enter Destination Directory : ")

    # Validate Source Directory
    if not os.path.isdir(SourceDir):
        print("Invalid Source Directory")
        return

    # Validate Destination Directory
    if not os.path.isdir(DestinationDir):
        print("Invalid Destination Directory")
        return

    print("Automatic File Copy Started...")

    # Schedule every 10 minutes
    schedule.every(10).minutes.do(CopyTextFiles,
                                  SourceDir,
                                  DestinationDir)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()