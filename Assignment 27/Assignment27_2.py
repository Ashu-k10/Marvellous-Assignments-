class BankAccount:

    #class variable
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def display(self):
        print("Amount Holder Name :",self.Name)
        print("Current Balance  :",self.Amount)

    def Deposit(self):
        value = float(input("Enter amount of deposit :"))

        if value > 0:
            self.Amount = self.Amount + value
            print("Amount withdrawn successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self):
        value = float(input("Enter amount of withdraw :"))

        if value <= 0:
            print("Invalid withdrawal amount")
        elif value <= self.Amount:
            self.Amount = self.Amount - value
            print("Amount withdrawn sucessfully")
        else:
            print("Insufficient balance")        

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    

obj1 = BankAccount("ABC",1000)
obj1.display()
obj1.Deposit()
obj1.withdraw()

obj2 = BankAccount("xyz",2000)
obj2.display()
obj2.Deposit()
obj2.withdraw()


        

