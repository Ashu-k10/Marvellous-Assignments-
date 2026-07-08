from functools import reduce 

# to find prime numbers
def filterX(No):
    if No < 2:
        return False
    
    for i in range(2, No):
        if No % i == 0: 
            return False
        
    return True

# multiply each by 2
def MapX(no):
    return no * 2

#to find maximum number from that number
def reduceX(x,y):
    if x > y:
        return x
    else:
        return y
    
def main():

    Data = [2,70,11,10,17,23,31,77]
    print("input list ",Data)

    FData = list(filter(filterX,Data))
    print("List after filter",FData)

    MData = list(filter(filterX,FData))
    print("List after filter",MData)

    if len(MData) > 0:
        ans = reduce(reduceX, MData)
    else:
        ans = 0

    print("Output of reduce is :", ans)

if __name__ == "__main__":
    main()
