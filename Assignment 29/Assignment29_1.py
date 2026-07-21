#Write a program which accepts a file name from the user and checks wjether that file exists in the current directory or not.
# Input : Demo.txt
# Expected Output : Display Whether Demo.txt exists or not

import os

def checkFile(filename):
    if os.path.exists(filename):
        print("File Present in current directory")
    else:
        print("File is not in current Directory")

def main():
    name = input("Enter the file name :")

    checkFile(name)
if __name__ == "__main__":
    main()





