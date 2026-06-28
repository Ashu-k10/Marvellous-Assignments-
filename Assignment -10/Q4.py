#Write an program which accepts one number and prints all even number till that number

def even(n):

    for n in range(1,n+1):
            if n * 2 == 0:
                 print(n,end=" ")

def main():
    ret = even(5)

if __name__ == "__main__":
    main()