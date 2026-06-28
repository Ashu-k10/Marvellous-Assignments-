# Q2.Write a program which contains one function named as ChkGreater() that accepts two numbers and prints the greater number.

def ChkGreater(No1,No2):

    if (No1 >= No2):      #used a if-else staement to consider the greater number here and 
        return No1
    else:
        return No2

def main():
    
    Ret = ChkGreater(10,20)              # Ret 10 >= 20 

    print("The greater value is :",Ret)    #Greater value is : 20 
    
if __name__ == "__main__":
    main()