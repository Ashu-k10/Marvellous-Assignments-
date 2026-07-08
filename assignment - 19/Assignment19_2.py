multiplication = lambda No1,No2 : No1 * No2  # Number1 x Number2

def main(): 
    value1 = int(input("Enter the first number :"))
    value2 = int(input("Enter the second number :"))
    ret = multiplication(value1,value2)

    print("The value of the number is :",ret)

if __name__ == "__main__":
    main()