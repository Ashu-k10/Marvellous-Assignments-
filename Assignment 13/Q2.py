# Write a program which accepts radius of circle and prints area of circle

def area(pi,r):

    sum = pi*r*r   # area of circle = pi x r2
    return sum

def main():
    value1 = int(input("Enter the value of the pi : "))
    value2 = int(input("Enter the value of the radius : "))

    ret = area(value1,value2)

    print("The area of the circle is :",ret)

if __name__ == main():
    main()
    