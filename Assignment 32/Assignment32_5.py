# Write a program that deletes all empty files from the specified directory every hour.

# The program should :
#       • Scan the directory recursively
#       • Detect files whose size is zero bytes
#       • Delete the empty files
#       • Store deleted file path in a log file
#       • Handle permission errors
# Test the program only on a sample directory 


import os
import schedule
import time
import datetime

def DeleteEmptyFiles(DirectoryPath):

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("DeleteLog.txt", "a") as logfile:

        logfile.write("\n" + "=" * 60 + "\n")
        logfile.write(f"Date & Time : {current_time}\n")

        for FolderName, SubFolders, FileNames in os.walk(DirectoryPath):

            for File in FileNames:

                FilePath = os.path.join(FolderName, File)

                try:

                    if os.path.getsize(FilePath) == 0:

                        os.remove(FilePath)

                        logfile.write(f"Deleted : {FilePath}\n")
                        print(f"Deleted : {FilePath}")

                except PermissionError:

                    logfile.write(f"Permission Denied : {FilePath}\n")
                    print(f"Permission Denied : {FilePath}")

                except Exception as e:

                    logfile.write(f"Error : {FilePath} --> {e}\n")
                    print(f"Error : {FilePath}")
                
        logfile.write("=" * 60 + "\n") 

def main():

    DirectoryPath = input("Enter Directory Path : ")

    if not os.path.isdir(DirectoryPath):
        print("Invalid Directory")
        return

    print("Empty File Monitor Started...")

    # Run every hour
    schedule.every().hour.do(DeleteEmptyFiles, DirectoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
      
