# Please follow below rules while designing automation script as
#  • Accept input through command line or through file\
#  • Display any message in log file instead of console
#  • For separate task define separate function
#  • For robustness handle every expected exception.
#  • Perform validations before taking any action.
#  • Create user defined modules to store the functionality

# 1. Design Automation script which accept directory name and mail id from user and create log   
#     Usage : ProInfo.py Demo Marvellousinfosystem@gmail.com

import psutil
import os
import sys
import time
import smtplib
from email.message import EmailMessage

SENDER = "yourgmail@gmail.com"
APP_PASSWORD = "your_app_password"

def CreateLog(dirname):

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    filename = os.path.join(
        dirname,
        "ProcessLog.log"
    )

    with open(filename, "w") as f:

        f.write("{:<30}{:<10}{}\n".format(
            "Process Name","PID","Username"))

        for process in psutil.process_iter(['pid','name','username']):
            try:
                f.write("{:<30}{:<10}{}\n".format(
                    process.info['name'],
                    process.info['pid'],
                    process.info['username']))
            except:
                pass

    return filename


def SendMail(receiver, filepath):

    msg = EmailMessage()
    msg["Subject"] = "Running Process Log"
    msg["From"] = SENDER
    msg["To"] = receiver

    msg.set_content("Attached is the process log.")

    with open(filepath,"rb") as f:
        data = f.read()

    msg.add_attachment(
        data,
        maintype="application",
        subtype="octet-stream",
        filename=os.path.basename(filepath)
    )

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(SENDER,APP_PASSWORD)
        smtp.send_message(msg)

    print("Mail Sent Successfully")


def main():

    if len(sys.argv) != 3:
        print("Usage : python ProcInfoLog.py Directory Email")
        return

    logfile = CreateLog(sys.argv[1])
    SendMail(sys.argv[2], logfile)

if __name__ == "__main__":
    main()