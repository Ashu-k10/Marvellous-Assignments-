class Numbers:

    # Constructor
    def __init__(self, Value):
        self.Value = Value

    # Check whether number is Prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    # Check whether number is Perfect
    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False

    # Display all factors
    def Factors(self):
        print("Factors are:", end=" ")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")

        print()

    # Return sum of all factors
    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum


# ---------------- Main ----------------

No1 = int(input("Enter first number: "))
obj1 = Numbers(No1)

print("Is Prime:", obj1.ChkPrime())
print("Is Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())


print("\n-----------------------------")


No2 = int(input("Enter second number: "))
obj2 = Numbers(No2)

print("Is Prime:", obj2.ChkPrime())
print("Is Perfect:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors:", obj2.SumFactors())

