# Write a program which accepts a file name from the user and displays the contents of the file line by line om the screen
#input : Demo.txt
#Expected output : Display each line of demo.txt one by one 

def Display(filename):

    try:
        filename = open("Demo.txt",'r')

        #for displaying file content inside
        for line in filename:
            print(line, end="")

        filename.close()

    except FileNotFoundError in filename:
        print("File does not exists")

def main():
    name = input("Enter file name :")
    Display(name)

if __name__ == "__main__":
    main()




