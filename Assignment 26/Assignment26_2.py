class Demo:
    pi = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = float(input("Enter the radius number :"))

    def CalculateArea(self):
        self.area = Demo.pi * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Demo.pi * self.radius

    def display(self):
        print("Radius of circle is :",self.radius)
        print("Area of circle is ",self.area)
        print("Circumference of circle is ",self.circumference)

obj1 = Demo()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.display()

obj2 = Demo()
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.display()



    
        

