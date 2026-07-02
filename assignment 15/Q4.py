# Write a lambda function using reduce() which accepts a list of numbers and returns a list of numbers and returns the addition of all elements.

from functools import reduce

addition = lambda x1,x2 : x1 + x2

def main():

    data = [1,2,3,4,5,6,7,8]
    add = reduce(addition,data)

    print("The addtion of the number is",add)

if __name__ == "__main__":
    main()
            

