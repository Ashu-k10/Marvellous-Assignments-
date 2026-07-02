# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

count = lambda No: No % 2 == 0

def main():
    data = [10,20,30,45,64,90,97]
    value = list(filter(count,data))

    print("The list of even numbers are :",len(value))
    print("The numbers are ",value)

if __name__ == "__main__":
    main()