# Write a program which accepts one number and prints binary equivalent

def Binary(No):
    BinaryNo = 0
    Place = 1

    while No > 0:
        Rem = No % 2
        BinaryNo = BinaryNo + (Rem * Place)
        Place = Place * 10
        No = No // 2

    print("Binary equivalent is:", BinaryNo)

def main():
    Value = int(input("Enter a number: "))
    Binary(Value)

if __name__ == "__main__":
    main()