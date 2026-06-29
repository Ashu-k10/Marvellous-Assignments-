# Write a program which accepts one number and checks whether it si perfect number or not.

def perfect(No):

    if No % 2 == 0:
        print("Perfect Number")
    else:
        print('Not a perfect number')

def main():
    value = int(input("Enter the Number : "))  # 6

    ret = perfect(value)      # 6 : Perfect Number

if __name__ == "__main__":
    main()
