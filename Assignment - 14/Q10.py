# Write a lambda function which accepts three number and returns largest number.

large = lambda no1,no2,no3 : no1 if no1 >= no2 and no1 >= no3 else (no2 if no2 >= no3 else no3)

def main():
    value1 = int(input("Enter your first Number :"))
    value2 = int(input("Enter your second Number :"))
    value3 = int(input("Enter your third Number :"))

    ret = large(value1,value2,value3)
    print("Largest number is:",ret)

if __name__ == "__main__":
    main()
