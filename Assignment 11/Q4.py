# Write an program which accepts one number and prints reverse of that number.

def reverse(no):

    sum = 0

    while no > 0:
        digit = no % 10
        sum = (sum * 10) + digit
        no = no // 10

    return sum
    
def main():
        
        print("Enter the number :")
        value = int(input())

        ret = reverse(value)

        print("Reversed number of the following is: ",ret)

if __name__ == "__main__":\
        main()


