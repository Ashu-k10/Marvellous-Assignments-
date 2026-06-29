# Write a program which accepts marks and display grades.

# >= 75 : distinction
# >= 60 : first class
# >= 50 : Second Class
# <= 50 : Fail
        
def Grades(Grade):

    if (Grade >= 75):
        print("Distinction")
    
    elif(Grade >= 60):
        print("First Class")

    elif(Grade >= 50):
        print('Second Class')
    
    elif(Grade <= 50):
        print("Fail")

    return Grade

def main():
    value = int(input("Enter Your Grade : "))
    ret = Grades(value)

if __name__ == "__main__":
    main()
