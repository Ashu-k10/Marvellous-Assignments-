
import threading

# Thread1 function
def DisplayForward():
    print("Numbers from 1 to 50 :")

    for i in range(1, 51):
        print(i, end=" ")

    print("\n")


# Thread2 function
def DisplayReverse():
    print("Numbers from 50 to 1 :")

    for i in range(50, 0, -1):
        print(i, end=" ")

    print()


def main():

    # Creating threads
    t1 = threading.Thread(target=DisplayForward, name="Thread1")
    t2 = threading.Thread(target=DisplayReverse, name="Thread2")

    # Start Thread1
    t1.start()

    # Wait until Thread1 finishes
    t1.join()

    # Start Thread2
    t2.start()

    # Wait until Thread2 finishes
    t2.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()