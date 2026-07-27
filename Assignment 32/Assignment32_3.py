# Write a program that reads and displays the contents of a specified text file every minute.
# Handles the following conditions:
#  • File does not exists
#  • File is empty
#  • Permission is denied
#  • File cannot be opened

import os
import schedule
import time

def ReadFile(FilePath):

    try:
        # Check if file exists
        if not os.path.exists(FilePath):
            print("Error : File does not exist.")
            return

        # Check if file is empty
        if os.path.getsize(FilePath) == 0:
            print("Error : File is empty.")
            return

        # Open and read file
        with open(FilePath, "r") as file:
            print("\n--------- File Contents ---------")
            print(file.read())
            print("---------------------------------\n")

    except PermissionError:
        print("Error : Permission denied.")

    except OSError:
        print("Error : File cannot be opened.")


def main():

    FilePath = input("Enter File Path : ")

    # Schedule every minute
    schedule.every(1).minutes.do(ReadFile, FilePath)

    print("File Monitoring Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()