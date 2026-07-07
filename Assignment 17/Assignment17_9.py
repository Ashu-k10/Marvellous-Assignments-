def digit(no):

    count = 0

    if no == 0:
        return 1
    
    if no < 0:
        no = -no
    
    while no > 0:
        count = count + 1
        no = no // 10

    return count

def main():
    value = int(input("Enter the number :"))
    ret = digit(value)

    print("Number of digits is :",ret)

if __name__ == "__main__":
    main()



