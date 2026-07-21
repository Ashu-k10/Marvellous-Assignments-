# Write a program which accepts two files names through command line argument and compares the contents of both files
#  - If both file contain the same contents, display Sucess
#  - Otherwisre display failure
# Input (Command Line) : Demo.txt Hello.txt
# Excepted Output : Sucess or Failure 

import sys 
import os 

def CompareFiles(file1,file2):
    try:
        f1 = open(file1,"r")
        f2 = open(file2,"r")

        data1 = f1.read()
        data2 = f2.read()

        f1.close()
        f2.close()

        if data1 == data2:
            print("Sucess")
        else:
            print("Failure")

    except FileNotFoundError:
        print("One or both files do not exists")

def main():
    if len(sys.argv) != 3:
        print("Usage : python program.py <file1> <file2>")
        return
    
    CompareFiles(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
