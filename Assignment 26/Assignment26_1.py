class Demo :
    value = 100

    def __init__(self,no1,no2):
        self.no1 = no1 
        self.no2 = no2

    #instance variable  
    def fun(self):
        print("fun()")
        print("No1 = ",self.no1)
        print("No2 = ",self.no2)

    def gun(self):
        print("gun()")
        print("No1 = ",self.no1)
        print("No2 = ",self.no2)

Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj1.gun()






    
