def display(No):
    Count = 0

    if No < 0:
        No = -No

    while No > 0:
        digit = No % 10
        Count = Count + digit
        No = No // 10

    return Count
    
def main():
    value = int(input("Enter the number :"))
    ret = display(value)
    print("The addition of digits are :",ret)

if __name__ == "__main__":
    main()
