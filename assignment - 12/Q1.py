# Write a program which accepts oen character and checks whether it is vowels or consonant

def char(Word):

    if Word == 'a' or Word == 'e' or Word == 'i' or Word == 'o' or Word == 'u':
        print("its Vowels")
    else:
        print("Consonant")

def main():
    value = input("Enter your word : ")  #Enter your word : a 
    ret = char(value)                    # it's vowels

if __name__ == "__main__":
    main()