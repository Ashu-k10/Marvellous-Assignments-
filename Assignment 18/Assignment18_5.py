import marvellousNum

def ListPrime(Arr):

    Sum = 0

    for i in Arr:
        if marvellousNum.ChkPrime(i):
            Sum = Sum + i

    return Sum


def main():

    print("Enter number of elements:")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Result = ListPrime(Data)

    print("Addition of prime numbers is:", Result)


if __name__ == "__main__":
    main()