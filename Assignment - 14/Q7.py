# Write a lambda function which accepts one number and return True if divisible by 5.

checknum = lambda No : (No % 5 == 0)

def main():
    value = int(input("Enter the number :"))

    ret = checknum(value)

    if(value % 5 == 0):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()

