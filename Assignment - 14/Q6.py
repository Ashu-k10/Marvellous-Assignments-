# Write a lambda function which accepts one number and return True if number is odd otherwise False.

Checkodd = lambda no1 : (no1 % 2 != 2)

def main():
    value = int(input('Enter the number :'))

    ret = Checkodd(value)

    if (value % 2 != 0):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()

