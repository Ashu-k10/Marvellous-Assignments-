#Write a program which accepts one number and checks whether it is prime or not.
  

def prime(No):

    if No <= 1:
        print("Not a prime number")
        return
    
    for i in range(2, No):
        if No % i == 0:
            print("Not a prime number :")
            return 

    print("Prime Number")

def main():
    value = int(input("Enter your Number : "))
    ret = prime(value)
   

if __name__ == "__main__":
    main()