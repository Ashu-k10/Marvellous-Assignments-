import threading

# Function to count lowercase letters
def Small(text):
    count = 0

    for ch in text:
        if ch.islower():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase Characters :", count)
    print()


# Function to count uppercase letters
def Capital(text):
    count = 0

    for ch in text:
        if ch.isupper():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase Characters :", count)
    print()


# Function to count digits
def Digits(text):
    count = 0

    for ch in text:
        if ch.isdigit():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)
    print()


def main():
    str1 = input("Enter a string : ")

    # Creating threads
    t1 = threading.Thread(target=Small, args=(str1,), name="small")
    t2 = threading.Thread(target=Capital, args=(str1,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(str1,), name="digits")

    # Starting threads
    t1.start()
    t2.start()
    t3.start()

    # Waiting for all threads to finish
    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()