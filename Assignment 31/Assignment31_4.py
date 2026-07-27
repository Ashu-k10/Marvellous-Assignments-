# Write a program that creates a new log file after every ten minutes.

# The filemname should contain the current date and time

# Example :
#          Marvellouslog_25_07_2026_16_30_00.txt
#          the file should contain:

# Log file created sucessfully 
# Creation Time : 25-07-2026 04:30:00 PM

import time
import datetime


def CreateLogFile():
    # Current date and time
    current_time = datetime.now()

    # Filename format
    filename = current_time.strftime("Marvellouslog_%d_%m_%Y_%H_%M_%S.txt")

    # Log message
    log_message = (
        "Log file created successfully\n"
        f"Creation Time : {current_time.strftime('%d-%m-%Y %I:%M:%S %p')}"
    )

    # Create file and write log
    with open(filename, "w") as file:
        file.write(log_message)

    print(f"{filename} created.")


def main():
    print("Log Generator Started...")

    while True:
        CreateLogFile()

        # Wait for 10 minutes (600 seconds)
        time.sleep(600)


if __name__ == "__main__":
    main()



