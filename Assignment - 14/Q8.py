# Write a lambda function which accepts two number and returns addtion

addition = lambda No1,No2: No1 + No2

def main():
    value1 = int(input("Enter the first number : "))
    value2 = int(input("Enter your Second Number :"))

    ret = addition(value1,value2)
    print("The addition of two number is : ",ret)

if __name__ == "__main__":
    main()
