# Write a program which accepts one number and check whetherit is divisible by 3 and 5

# In def Function 

def division(No):
    if (No % 5 & No % 2):
        print("Divisible by 3 & 5")
    else:
        print("Not divisible by 3 & 5")

    return No

def main(): 
    print("Your Number is : ",ret)
    ret = division(10)
    
if __name__ == "__main__":
    main()

# In Lamda Function 

division = lambda x : x*x*x

def main():
    print("Your value is :",ret)
    ret =  division(10)

if __name__ == "__main__":
    main()