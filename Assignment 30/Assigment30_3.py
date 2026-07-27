# Write a program that schedules a function to print
# Coding kar...!
# every 30 minutes

import time
import datetime
import schedule

def display():
    print("Coding kar ...")

def main():
    border = "-"*40

    print(border)
    print("CHALLL !! Aab")
    print(border)

    schedule.every(30).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
