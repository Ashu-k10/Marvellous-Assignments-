# Write a program which accepts one number and prints its factors.

def factors(No):

    print("Factors are:")

    for i in range(1, No + 1):
        if No % 1 == 0:
            print(i)


def main():
    value = int(input("Enter the number: "))
    factors(value)

if __name__ == "__main__":
    main()