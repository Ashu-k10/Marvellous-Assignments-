def Factorial(No):
    Fact = 1

    for i in range(1, No):
        Fact = Fact * i

    return Fact

def main():

    ret = Factorial(5)
    print("Factorial is:",ret)

if __name__ == "__main__":
    main()