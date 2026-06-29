#Write a program which accepts length and width of rectangle and prints area.

def area(len,width):
    sum = len * width    # Area of reactangle = Length x Width
    return sum 

def main():
    value1 = int(input("Enter the value of the length: "))
    value2 = int(input("Enter the value of the breadth: "))

    ret = area(value1,value2)

    print("The area of rectangle is",ret)  

if __name__ == "__main__":
    main()

