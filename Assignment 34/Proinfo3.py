# Please follow below rules while designing automation script as
#  • Accept input through command line or through file\
#  • Display any message in log file instead of console
#  • For separate task define separate function
#  • For robustness handle every expected exception.
#  • Perform validations before taking any action.
#  • Create user defined modules to store the functionality

# 2. Design Automation script which Accept directory name from user and create log file in that directory which contains info of running processes as it name,PID,Username
#     Usage : ProInfo.py Demo

import psutil
import os
import sys
import time

def CreateLog(dirname):

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    filename = os.path.join(
        dirname,
        "ProcessLog_" +
        time.strftime("%Y%m%d_%H%M%S") +
        ".log"
    )

    with open(filename, "w") as f:

        f.write("{:<30}{:<10}{}\n".format(
            "Process Name","PID","Username"))

        f.write("-"*60+"\n")

        for process in psutil.process_iter(['pid','name','username']):
            try:
                f.write("{:<30}{:<10}{}\n".format(
                    process.info['name'],
                    process.info['pid'],
                    process.info['username']))
            except:
                pass

    print("Log created :", filename)

def main():

    if len(sys.argv) != 2:
        print("Usage : python ProcInfoLog.py DirectoryName")
        return

    CreateLog(sys.argv[1])

if __name__ == "__main__":
    main()