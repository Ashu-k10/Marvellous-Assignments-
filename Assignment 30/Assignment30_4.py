import schedule
import time

def Greeting():
    print("Namaskar...")

def main():

    schedule.every().day.at("09:00").do(Greeting)

    print("Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()