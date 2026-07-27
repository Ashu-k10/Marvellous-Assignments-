# Write a script that schedule the following tasks:
#   • print Lunch Time ! every day at 1:00 pm
#   • print Wrap up work every day at 6:00 pm
# Both task should be handled by separate functions
 
import schedule
import time

def Lunch():
    print("Lunch Time!")

def WrapUp():
    print("Wrap up work")

def main():

    schedule.every().day.at("13:00").do(Lunch)

    schedule.every().day.at("18:00").do(WrapUp)

    print("Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()