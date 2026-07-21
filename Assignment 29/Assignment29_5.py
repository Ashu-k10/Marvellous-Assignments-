# Write a program which accepts a file name and one using from the user and returns the frequency (count of occurence) of that string in the file
#  Input : Demo.txt Marvellous 
#  Excepted Output : Count how many times "Marvellous" appears in Demo.txt

def CountFrequency(FileName, Word):
    try:
        file = open(FileName, "r")

        data = file.read()
        file.close()

        words = data.split()

        count = 0
        for w in words:
            if w == Word:
                count += 1

        print(f'"{Word}" appears {count} times in {FileName}.')

    except FileNotFoundError:
        print("File does not exist.")


def main():
    Name = input("Enter file name: ")
    Word = input("Enter word to search: ")

    CountFrequency(Name, Word)


if __name__ == "__main__":
    main()