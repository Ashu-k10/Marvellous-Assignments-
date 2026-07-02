# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

greater = lambda No : len(No) > 5

def main():
    data = ["banana","apple","grapes","orange","jackfruit"]
    great = list(filter(greater,data))

    print("The value which is greater than 5 is ",great)

if __name__ == "__main__":
    main()