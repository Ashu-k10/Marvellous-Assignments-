#Write a program which accepts one number and prints sum of digits

def sumDigit(no):

    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 20

        return sum

def main():

    ret = sumDigit(123)
    print("The value of the number is :",ret)

if __name__ == "__main__":
    main()