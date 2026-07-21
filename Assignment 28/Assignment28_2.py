# Write a program which accepts a file name from the user and counts how many lines are presents in the file.
# input : Demo.txt
# Expected Output : Total number of lines in Demo.txt 

def countwords(fobj):

    try:
        fobj = open('Demo.txt','r')

        count = 0
        for line in fobj:
            words = line.split()
            count += len(words)

        fobj.close()
        print("Total numbers of words in Demo.txt",count)

    except FileNotFoundError as fobj:
        print("File does not exist")

def main():
    Name = input("Enter file name :")
    countwords(Name)

if __name__ == "__main__":
    main()