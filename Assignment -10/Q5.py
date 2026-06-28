#Write a program which accepts one number anf prints all off nunmbers till that number.

def odd(n):

    for n in range(1,n+1):
        if n % 2 != 0:
            print(n,end=" ")

def main():
    value = int(input("Enter your number :"))
    ret = odd(value)

if __name__ == "__main__":
    main()