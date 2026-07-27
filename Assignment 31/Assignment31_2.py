# Create a function named:
#        DisplayMessage(message) : Schedule the function using:

#        schedule.every(5).seconds.do(displayMessage,message):
#        The message should be accepted from the user

import schedule
import time

def DisplayMessage(message):
    print(message)

def main():
    border ="-"*20

    message = (input("Enter the message : "))
    
    schedule.every(5).seconds.do(DisplayMessage,message)
    print(border+"Automation have started"+border)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
