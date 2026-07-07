def display(no):

    for i in range(1,no+1):
        for j in range(no):
          print(j,end="")
        print()

def main():
    
    ret = display(5)

if __name__== "__main__":
    main()
     