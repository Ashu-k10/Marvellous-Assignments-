# Write a program which accepts two files name from the user
#   - First file is an existing file
#   - Second file is a new file
# Copy all contents from the first file into the second file.
# Input : ABC.txt Demo.txt
# Excepted Output : Contents of ABC.txt copied into Demo.txt

def file(Existing,newfile):
    try:

        file1 = open(Existing,'r')
        data = file1.read()
        file1.close()

        file2 = open(newfile,"w")
        file2.write(data)
        file2.close

        print("Contents copied sucessfully.")

    except FileNotFoundError:
        print("Source files does not exist.")

def main():
    Existing = input("Enter existing file : ")
    newfile = input("Enter newfile : ")

    file(Existing,newfile)

if __name__ == "__main__":
    main()

