# Please follow below rules while designing automation script as
#  • Accept input through command line or through file\
#  • Display any message in log file instead of console
#  • For separate task define separate function
#  • For robustness handle every expected exception.
#  • Perform validations before taking any action.
#  • Create user defined modules to store the functionality

# 1. Design Automation script which display info of running processes as its names,PID,Username.
#     Usage : ProInfo.py

import psutil

def displayprocess():
    print("{:<30}{:<10}{}".format("Process Name","PID","Username"))
    print("-"*60)

    for process in psutil.process_iter(['pid','name','username']):
        try:
            print("{:<30}{:<10}{}".format(
                process.info['name'],
                process.info['pid'],
                process.info['username']))
        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

def main():
    displayprocess()

if __name__ == "__main__":
    main()
