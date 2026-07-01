# Write a lambda function which accpets two numbers and return maximum number.

max = lambda no1,no2: no1 if no1 > no2 else no2

def main():
    value1 = int(input("Enter your first number : "))
    value2 = int(input("Enter your second number : "))

    ret = max(value1,value2)
    print("The Maximum number : ",ret)

if __name__ == "__main__":
    main()