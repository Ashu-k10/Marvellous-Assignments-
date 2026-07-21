#Write a program which accepts a file name from the user and counts how many lines are present in the file.
#Input : Demo.txt
#Except Output : total number of lines in Demo.txt

def countfile(fobj):

    try:
        fobj = open("Demo.txt","r")  # r for reading 

        count = 0     #count numbers of lines
        for line in fobj:
            count += 1

        fobj.close()
        print("total number of lines: ",count)

    except  FileNotFoundError as fobj:
        print("File doesnt exist")

def main():

    Name = input("Enter file name :")
    countfile(Name)

if __name__ == "__main__":
    main()
        