import Arthematic as Arth

def main():
    Value1 = int(input("Enter your First number : "))
    Value2 = int(input("Enter your Second Number : "))

    ret1 = Arth.Add(Value1,Value2)
    ret2 = Arth.Sub(Value1,Value2)
    ret3 = Arth.Mult(Value1,Value2)
    ret4 = Arth.Div(Value1,Value2)

    print("The value of addition is:",ret1)
    print("The value of substraction is:",ret2)
    print("The value of division is:",ret4)
    print("The value of multiplication is:",ret3)

if __name__ == "__main__":
    main()