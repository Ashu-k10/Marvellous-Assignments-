# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

product = lambda No1,No2 : No1 * No2

def main():
    data = [20,40,3,8]
    value = reduce(product,data)

    print("The product of the data is",value)

if __name__ == "__main__":
    main()




