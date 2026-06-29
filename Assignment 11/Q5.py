# Write an program which accepts one number and checks whether it is palindrome or not

def palindrome(word):

    reverse = ""

    for ch in word:
        reverse = ch + reverse

    if word == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")


def main():
    value = (input("Enter your number :"))
    palindrome(value)

if __name__ == "__main__":
    main()


        