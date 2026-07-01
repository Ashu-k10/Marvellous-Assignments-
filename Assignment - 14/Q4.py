# Write a lambda function which accepts two number and returns minimum number.

Min = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    value1 = int(input("Enter the first number :"))
    value2 = int(input("Enter the second number :"))

    ret = Min(value1,value2)
    
    print("The Minimum number of the following is :",ret)

if __name__ == "__main__":
    main()
    
