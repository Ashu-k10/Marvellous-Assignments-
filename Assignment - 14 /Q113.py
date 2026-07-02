# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number,

square = lambda x: x * x

def main ():
    Numbers = [1,2,3,4,5,6]
    squares = list(map(square,Numbers))

    print(squares)

if __name__ == "__main__":
    main()
