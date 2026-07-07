def MaxDigit(No):
    Max = 0

    if No < 0:
        No = -No

    while No > 0:
        Digit = No % 10

        if Digit > Max:
            Max = Digit

        No = No // 10

    return Max


def main():
    print("Enter a number:")
    Value = int(input())

    Result = MaxDigit(Value)

    print("Maximum digit is:", Result)


if __name__ == "__main__":
    main()