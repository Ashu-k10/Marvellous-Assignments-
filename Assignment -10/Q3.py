#Write a program which accepts one number and prints factorial of that number

def factorial(n):
    sum = 1

    for i in range(1,n +1):
        sum = sum * i

    return sum

def main():
    
    ret = factorial(5)

    print(ret)

if __name__ == "__main__":
    main()

