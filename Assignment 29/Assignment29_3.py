import sys

def copyfile(source):
    
    try:
        file1 = open(source,"r")
        data = file1.read()
        file1.close()

        file2 = open("Demo.txt","w")
        file2.write(data)
        file2.close()

        print("Contents copied sucessfully into it")

    except:
        print("Source file does not exist.")

def main():
    if len(sys.argv) != 2:
        print("Usage : python program.py <SourceFile>")
        return 
    
    copyfile(sys.argv[1])

if __name__ == '__main__':
    main()

