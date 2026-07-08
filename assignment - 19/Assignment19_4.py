from functools import reduce

# Function to filter numbers
def FilterX(value):
    return value % 2 == 0

# Function to square of the number
def MapX(value):
    return value * value

# Function to addtion of the numbers
def ReduceX(x, y):
    return x + y

def main():
    Data = [5,2,3,4,3,4,1,2,8,10]
    print("The Data is ",Data)

    Fdata = list(filter(FilterX,Data))
    print("list after filter :",Fdata)

    Mdata = list(map(MapX,Fdata))
    print("List after map ",Mdata)

    if len(Mdata) > 0:
        ans = reduce(ReduceX,Mdata)
    else:
        ans = 0

    print("output of reduce is : ",ans)

if __name__ == "__main__":
    main()
