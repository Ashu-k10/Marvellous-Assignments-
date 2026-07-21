# Write a program which accepts a file name from the user , opens the file, and display the entire contents on the console.
# Input : Demo.txt
# Expected Output : Display contents of Demo.txt on console

def Display(filename):
    try:
        file = open(filename,"r")

        data = file.read()
        print(data)

        file.close()

    except FileNotFoundError:
        print("File does not exist.")

def main():
    Name = input("Enter file name: ")
    Display(Name)

if __name__ == "__main__":
    main()