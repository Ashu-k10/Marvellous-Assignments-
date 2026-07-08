from functools import reduce

# Function to filter numbers
def FilterX(value):
    return value >= 70 and value <= 90

# Function to increase number by 10
def MapX(value):
    return value + 10

# Function to calculate product
def ReduceX(x, y):
    return x * y

def main():
    
    data = [4,34,36,76,68,24,89,23,86,90,45,70]
    print("Original List :", data)

    fdata = list(filter(FilterX, data))
    print("Filtered List :", fdata)

    mdata = list(map(MapX, fdata))
    print("Mapped List   :", mdata)

    if len(mdata) > 0:
        ans = reduce(ReduceX, mdata)
    else:
        ans = 0

    print("Product :", ans)

if __name__ == "__main__":
    main()