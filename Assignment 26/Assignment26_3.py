class Demo:
   
    def __init__(self):
        self.no1 = 0
        self.no2 = 0
    
    def Accept(self):
        self.no1 = int(input("Enter the first number :"))
        self.no2 = int(input("Enter the second number :"))

    def Addition(self):
        return self.no1 + self.no2 

    def substraction(self):
        return self.no1 - self.no2 

    def Multiplication(self):
        return self.no1 * self.no2 

    def division(self):
        if self.no2 == 0:
            return "Divison by zero is not possible."
        return self.no1 / self.no2
    
obj1 = Demo()
obj1.Accept()

print("Addition :",obj1.Addition())
print("Substraction :",obj1.substraction())
print("multiplication :",obj1.Multiplication())
print("division :",obj1.division())

print("\n---------------------------------")

obj2 = Demo()
obj2.Accept()

print("Addition :",obj2.Addition())
print("Substraction :",obj2.substraction())
print("multiplication :",obj2.Multiplication())
print("division :",obj2.division())

    

        
