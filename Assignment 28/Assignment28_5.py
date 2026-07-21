#Write a program which accepts a file name and a word from the user and checks whether that word is present the file or not
#input : Demo.txt Marvellous
#Expected Output : Display whether the word Marvellous is found in Demo.txt or not

def Searchword(filename,word):
    
    try:
        file = open(filename,'r')
        data = file.read()
        file.close()

        if word in data :
            print(word,"Found in file")
        else:
            print(word,"File in not found")

    except FileNotFoundError:
        print("Source files does not exist.")

def main():
    Name = input("Enter the name of file :")
    word = input("Enter the word :")

    Searchword(Name,word)

if __name__ =="__main__":
    main()