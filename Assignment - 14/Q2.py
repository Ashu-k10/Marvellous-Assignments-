#Write a lambda function which accepts two numbers and returns cube of that number.

cube = lambda No : No * No * No

def main():
    value = int(input("Enter the number : "))

    ret = cube(value)

    print("The value of the number is :",ret)

if __name__ == "__main__":
    main()