# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce
max = lambda No1,No2 : No1 if No1 > No2 else No2

def main():

    data = [1,2,3,4,5,6,7,8,9]
    maximum = reduce(max,data)
    
    print("The maximum element of the number is :",maximum)

if __name__ == "__main__":
    main()
