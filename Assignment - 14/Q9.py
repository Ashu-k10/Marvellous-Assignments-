# Write a lambda function which accepts two numbers and returns multiplication.

multiplication = lambda No1,No2 : No1 * No2

def main():
    value1 = int(input("Enter your First Number : "))
    value2 = int(input("Enter your Second Number : "))

    ret = multiplication(value1,value2)
    print("The multiplication of the number : ",ret)

if __name__ == "__main__":
    main()
    