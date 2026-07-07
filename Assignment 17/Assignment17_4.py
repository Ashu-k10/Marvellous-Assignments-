def additionfact(No):
    Sum = 0
    

    for i in range(1, No+1):
        Sum = Sum + i
        
    return Sum

def main():

    ret = additionfact(12)

    print("The value is :",ret)

if __name__ == "__main__":
    main()
