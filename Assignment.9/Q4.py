#Write a program which accepts one number and prints cube of that number.
# In def function :
def cube(x):
    x = x * x * x
    return x 

def main():
    value = int(input("Enter the value of the number : "))
    ret = cube(value)
    print("The cube of your Number is : ",ret)

if __name__ == "__main__":
    main()

# In Lambda Function 

cube = lambda x : x * x * x

def main():
    value = int(input("Enter the value of the number"))
    ret = cube(value)
    print("The value of the number is : ",ret)

if __name__ == "__main__":
    main()