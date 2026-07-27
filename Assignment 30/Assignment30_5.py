# Schedule a task that execute every five minutes and append current date & time into Marvellous.txt

import schedule
import time
import datetime

def WriteLog():

    file = open("Marvellous.txt", "a")

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    file.write(f"Task executed at: {current_time}\n")

    file.close()

    print("Entry Added")

def main():

    schedule.every(5).minutes.do(WriteLog)

    print("Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()