def prime(No):

    if(No <= 1):
        return False
    
    else:
        for i in range(2,No):
            if No % i == 0:
                return False
        
        return True
                
def main():
    value = int(input("Enter the number : "))
    
    if prime(value):
        print("it is prime")
    else:
        print("Not a prime number")

if __name__ == "__main__":
    main()