# Write a lambda function using filter() which accepts a list of numbers and returns a list of even number.

evenum = lambda x : x % 2 == 0

def main():

    data = [1,2,3,4,5,6,7]
    even = list(filter(evenum,data))

    print(even)

if __name__ == "__main__":
    main()