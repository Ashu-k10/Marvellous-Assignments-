#Write a program which accepts one number and prints Sum of first N natural numbers 

def Naturalnumber(No):
    sum = No * (No + 1) // 2   # here we use the formula of N = N(N+1)/2
    return sum

def main():
    value = int(input("Enter your Value here : "))
    ret = Naturalnumber(value)          # return value 
    
    print("The value of the number is : ",ret)

if __name__ == "__main__":   # The Starter Pack 
    main()