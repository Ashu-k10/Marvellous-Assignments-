def Frequency(Arr, No):
    Count = 0

    for i in Arr:
        if i == No:
            Count = Count + 1

    return Count

def main():
    print("Enter the number of elements:")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Enter the number to search:")
    Search = int(input())

    Result = Frequency(Data, Search)

    print("Frequency of", Search, "is:", Result)


if __name__ == "__main__":
    main()