# Please follow below rules while designing automation script as
#  • Accept input through command line or through file\
#  • Display any message in log file instead of console
#  • For separate task define separate function
#  • For robustness handle every expected exception.
#  • Perform validations before taking any action.
#  • Create user defined modules to store the functionality

# 1. Design Automation script which Accept process name and display information of that process if its running 
#     Usage : ProInfo.py Notepad

import psutil
import sys

def FindProcess(name):

    found = False

    for process in psutil.process_iter(['pid','name','username']):
        try:
            if process.info['name'].lower() == name.lower():
                found = True
                print("\nProcess Found")
                print("Name :", process.info['name'])
                print("PID :", process.info['pid'])
                print("User :", process.info['username'])

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    if not found:
        print("Process not running")

def main():

    if len(sys.argv) != 2:
        print("Usage : python ProcInfo.py ProcessName")
        return

    FindProcess(sys.argv[1])

if __name__ == "__main__":
    main()