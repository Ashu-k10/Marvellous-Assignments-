# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

minimum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    data = [1,2,3,4,5,6,7,8]
    min = reduce(minimum,data)

    print("The minimum element number is ",min)

if __name__ == "__main__":
    main()
