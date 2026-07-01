# Write a lambda function which accepts one number and returns square of that number 

Square = lambda No : No * No

def main():
    
    value =int(input('Enter your Number :'))
    
    ret = Square(value)
    print("Square of the number is :",ret)

if __name__ == "__main__":
    main()