def display(No):

    if (No > 0):
        print("Positive number")
    elif(No < 0):
        print("Negative Number")
    else:
        print("Zero")


def main():
    value = int(input("Enter your Number : "))

    ret = display(value)
    
if __name__ == "__main__":
    main()