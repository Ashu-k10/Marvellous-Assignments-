# Write a program that creates a new text file every minute.
# The filename should contain the current timestamp
# Example : 
#         File_25_07_2026_16_30_00.txt
# Write the following info into the file:
#     • Filename 
#     • Creation date
#     • Creation time

import schedule
import time
import datetime

def CreateFile():

    current_time = datetime.now()

    # File name with timestamp
    filename = current_time.strftime("File_%d_%m_%Y_%H_%M_%S.txt")

    with open(filename, "w") as file:
        file.write(f"Filename : {filename}\n")
        file.write(f"Creation Date : {current_time.strftime('%d-%m-%Y')}\n")
        file.write(f"Creation Time : {current_time.strftime('%I:%M:%S %p')}\n")

    print(f"{filename} created successfully.")

schedule.every(1).minutes.do(CreateFile)

def main():

    print("File Creation Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()