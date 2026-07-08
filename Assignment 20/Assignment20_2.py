import threading

def EvenFactor(no):

    sum_even = 0

    print("Even Factors are : ", end=" ")

    for i in range(1, no + 1):
        if (no % i == 0) and (i % 2 == 0):
            print(i, end=" ")
            sum_even = sum_even + i

    print("\nSum of Even Factors :", sum_even)


# Function to find odd factors
def OddFactor(no):

    sum_odd = 0

    print("Odd Factors are : ", end=" ")

    for i in range(1, no + 1):
        if (no % i == 0) and (i % 2 != 0):
            print(i, end=" ")
            sum_odd = sum_odd + i

    print("\nSum of Odd Factors :", sum_odd)

def main():
    num = int(input("Enter a number : "))

    t1 = threading.Thread(target=EvenFactor, args=(num,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(num,), name="OddFactor")
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()