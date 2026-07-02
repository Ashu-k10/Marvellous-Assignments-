# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd number.

odd = lambda x : x % 2 != 0

def main():
    data = [1,2,3,4,5,6,7,8,9]
    value = list(filter(odd,data))

    print(value)

if __name__ == "__main__":
    main()