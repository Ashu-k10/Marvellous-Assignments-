power = lambda No : 2 ** No    # 2 raise to the number 

def main():
    value = int(input("Enter the number : "))
    ret = power(value)

    print("The power of the number is :",ret)

if __name__ == "__main__":
    main()
