#Write a program which accepts one number and prints count of digits in that number 

def CountDigits(No):

    Count = 0

    while No > 0:               # Used while loop to count the digits of a number
        Count = Count + 1
        No = No // 10

    return Count


def main():
 
    Ret = CountDigits(7521)  
    
    print("Number of digits is:", Ret)  # digits are 4 here

if __name__ == "__main__":
    main()
    