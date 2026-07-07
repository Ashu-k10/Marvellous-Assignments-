def addition(no):
    list = []
    
    for i in range(no):
        num = int(input("Enter number: "))
        list.append(num)

    return list

def main():
    n = int(input("Enter how many numbers: "))

    numbers = addition(n)

    total = 0
    for i in numbers:
        total = total + i

    print("list=",numbers)
    print("Addtion of all elements =",total)

if __name__ == "__main__":
    main()