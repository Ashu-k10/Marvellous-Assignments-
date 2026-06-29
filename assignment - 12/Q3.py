# Write a program which accepts two numbers and prints addtion, substraction , multiplication and division

def addtion(No1,No2):
    sum = No1 + No2
    return sum

def substraction(No1,No2):
    sum = No1 - No2
    return sum

def multiplication(No1,No2):
    sum = No1 *  No2
    return sum

def Division(No1,No2):
    sum = No1 // No2
    return sum

def main():
    Value1 = int(input("Enter your first Number : "))
    Value2 = int(input("Enter your second number :"))

    ret1 = addtion(Value1,Value2)
    ret2 = substraction(Value1,Value2)
    ret3 = multiplication(Value1,Value2)
    ret4 = Division(Value1,Value2)

    print("The addition of the number is :",ret1)
    print("The substraction of the number is :",ret2)
    print("The division of the number is :",ret3)
    print("The Multiplication of the number is :",ret4)

if __name__ == "__main__":    #starter pack
    main()