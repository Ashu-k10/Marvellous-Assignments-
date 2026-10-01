import math
import numpy as np

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def Weightsum(input,weights,bias):
    input = np.array(input)
    print("Inputs are :",input)
 
    weights = np.array(weights)
    print("Weights are :",weights)

    print("Bias are :",bias)

    z = np.dot(input,weights) + bias
    print("z : ",z)

    return z

def sigmoidFormula(inputs,weights,bias):

    z = 0

    for i in range(len(inputs)):
        z = z + (inputs[i] * weights[i])

        z = z + bias

        y = sigmoid(z)
    return y 

def main():

    input = (2, 3)
    weights = (0.4, 0.6)
    bias = 0.5

    result1 = Weightsum(input, weights, bias)
    print("Weighted Sum :",result1)

    result2 = sigmoidFormula(input,weights,bias)
    print("Sigmoid is :",result2)

    print("Output is between 0 to 1 :", 0<= result2 <= 1)

    if result2 >= 0.5:
        print("Output is closer to 1")
    else:
        print("Output is closer to 0")

if __name__ == "__main__":
    main()
