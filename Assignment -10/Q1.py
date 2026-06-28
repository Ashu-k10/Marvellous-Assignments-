# Write a program which accepts one number and prints multiplication table of that number

def Multiplication(No):

    for No in range(0,44,4):  # start = 0 , end = 44 , diff = 4
        print(No)
    return No

def main():
    ret = Multiplication(4)   #returned value
    
if __name__ == "__main__":  # the Starter pack
    main()