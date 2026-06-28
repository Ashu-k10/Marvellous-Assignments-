#Write a program which accepts one number and prints square of that number 

#In lambda Functional Programming method 

square = lambda x : (x * x)
        
def main():
    value = int(input("Enter the Number : "))
    ret = square(value)  

    print("The Square of your Number is ",ret)

if __name__ == "__main__":
    main()


# Now using Def function 

def square(x):
    x = x * x
    return x

def main():
    value = int(input("Enter the Number : "))
    ret = square(value)  

    print("The Square of your Number is ",ret)

if __name__ == "__main__":
    main()
