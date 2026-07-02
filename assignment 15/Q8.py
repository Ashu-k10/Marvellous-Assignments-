# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 & 5.

divisible = lambda No :( No % 3 == 0 & No % 5 == 0 )

def main():
    data = [15,25,30,45,60,80]
    value = list(filter(divisible,data))

    print("The number which are divisible by 3 & 5 are ",value)

if __name__ == "__main__":
    main()