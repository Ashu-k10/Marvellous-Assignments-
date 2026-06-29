# Write a program which accepts one number and prints that many numbers in reverse order

def number(No):
    for i in range(No, 0,-1):
        print(i, end=" ")
        

def main():
    value = int(input("Enter the number :"))
    ret1 = number(value)

    print("The value of the following : ",ret1)

if __name__ == "__main__":
    main()
