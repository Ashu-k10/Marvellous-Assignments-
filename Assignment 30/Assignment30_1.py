#Write a program that prints:
# jay ganesh.....
# every two seconds
# Use: Schedule.every(2).seconds.do(...)
#Expected output : jai Ganesh...
#                  jai Ganesh...
#                  jai Ganesh...

import schedule
import time
import datetime

def display():
    print("Jai Ganesh....")

def main():
    border = "-"*40
    print(border)
    print("Automation Script started")
    print(border)

    schedule.every(2).seconds.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

    
    
