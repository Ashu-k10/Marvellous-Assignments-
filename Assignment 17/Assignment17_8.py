def Display(No):
    for i in range(1, No + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    Value = int(input("Enter a number:"))
    Display(Value)

if __name__ == "__main__":
    main()