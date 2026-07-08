import threading

# Global variables to store results
sum_result = 0
product_result = 1

# Function to calculate sum
def SumList(data):
    global sum_result

    for i in data:
        sum_result += i


# Function to calculate product
def ProductList(data):
    global product_result

    for i in data:
        product_result *= i


def main():
    n = int(input("Enter number of elements : "))

    arr = []

    print("Enter the elements :")
    for i in range(n):
        value = int(input())
        arr.append(value)

    # Creating threads
    t1 = threading.Thread(target=SumList, args=(arr,), name="Thread1")
    t2 = threading.Thread(target=ProductList, args=(arr,), name="Thread2")

    # Starting threads
    t1.start()
    t2.start()

    # Waiting for both threads to complete
    t1.join()
    t2.join()

    # Display results in main thread
    print("\nSum of Elements :", sum_result)
    print("Product of Elements :", product_result)


if __name__ == "__main__":
    main()