import threading

# Function to extract even numbers
def EvenList(data):
    even = []
    sum_even = 0

    for i in data:
        if i % 2 == 0:
            even.append(i)
            sum_even += i

    print("Even Numbers :", even)
    print("Sum of Even Numbers :", sum_even)


# Function to extract odd numbers
def OddList(data):
    odd = []
    sum_odd = 0

    for i in data:
        if i % 2 != 0:
            odd.append(i)
            sum_odd += i

    print("Odd Numbers :", odd)
    print("Sum of Odd Numbers :", sum_odd)


def main():
    n = int(input("Enter number of elements : "))

    arr = []

    print("Enter the elements :")
    for i in range(n):
        value = int(input())
        arr.append(value)

    # Creating threads
    t1 = threading.Thread(target=EvenList, args=(arr,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(arr,), name="OddList")

    # Starting threads
    t1.start()
    t2.start()

    # Waiting for both threads to finish
    t1.join()
    t2.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()