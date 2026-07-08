
import threading

# Function to check whether a number is prime
def CheckPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


# Thread function to display prime numbers
def Prime(data):
    print("Prime Numbers :")

    for num in data:
        if CheckPrime(num):
            print(num, end=" ")

    print("\n")


# Thread function to display non-prime numbers
def NonPrime(data):
    print("Non-Prime Numbers :")

    for num in data:
        if not CheckPrime(num):
            print(num, end=" ")

    print()


def main():
    n = int(input("Enter number of elements : "))

    arr = []

    print("Enter the elements :")
    for i in range(n):
        value = int(input())
        arr.append(value)

    # Creating threads
    t1 = threading.Thread(target=Prime, args=(arr,), name="prime")
    t2 = threading.Thread(target=NonPrime, args=(arr,), name="Non-prime")

    # Starting threads
    t1.start()
    t2.start()

    # Waiting for both threads to complete
    t1.join()
    t2.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()
