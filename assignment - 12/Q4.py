# Write a program which accepts one number and prints that many numbers starting from 1

def numbers(No):

    for i in range(1, No + 1):
        print(i)

def main():

    Value = int(input("Enter a number :"))
    numbers(Value)

if __name__ == "__main__":
    main()