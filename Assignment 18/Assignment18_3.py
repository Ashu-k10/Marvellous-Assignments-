def MinDigit(No):
    Min = 9
    
    if No < 0:
        No = -No

    if No == 0:
        return 0

    while No > 0:
        Digit = No % 10

        if Digit < Min:
            Min = Digit

        No = No // 10

    return Min


def main():
    Value = int(input("Enter the number : "))
    Ret = MinDigit(Value)

    print("Miniimum digit is:", Ret)


if __name__ == "__main__":
    main()