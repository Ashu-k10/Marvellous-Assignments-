# Write a program that schedules the following messages:
#       • Monday at 9:00 AM : Start your weekly goals
#       • Wednesday at 5:00 PM : Review your Weekly program
#       • Friday at 6:00 PM : Weekly work completed

# Use :
#       Schedule.every().monday.at(..)
#       Schedule.every().Wednesday.at(..)
#       Schedule.every().friday.at(..)


import schedule
import time
import datetime

def MondayTask():
    print(f"[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] Start your weekly goals")


def WednesdayTask():
    print(f"[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] Review your Weekly program")


def FridayTask():
    print(f"[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] Weekly work completed")

schedule.every().monday.at("09:00").do(MondayTask)

schedule.every().wednesday.at("17:00").do(WednesdayTask)

schedule.every().friday.at("18:00").do(FridayTask)

def main():
    print("Weekly Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()