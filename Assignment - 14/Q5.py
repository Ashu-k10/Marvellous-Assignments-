# Write a lambda function which accepts one number and returns True if number is even otherwise false.

Checkeven = lambda No :(No % 2 == 0)

def main():
    value = int(input("Enter the number : "))
    
    Checkeven(value)

    if(value % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number") 

if __name__ == "__main__":
    main()   