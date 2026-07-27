# Write a python program that displays the current date and time after every one minute.
# Use the datatime module
# Expected output : Current Date and Time : 25-07-2026 04:30:00 PM

import schedule
import datetime
import time

def display():
    print("Current Date and Time :",datetime.datetime.now())

def main():
    border = "-"*40
    print(border)
    print("Automation script started here")
    print(border)

    schedule.every(1).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    


