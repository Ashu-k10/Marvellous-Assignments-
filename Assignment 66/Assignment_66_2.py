import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. Sigmoid Activation Function
# ------------------------------------------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# ------------------------------------------------------------
# 2. Tanh Activation Function
# ------------------------------------------------------------
def tanh(x):
    return np.tanh(x)


# ------------------------------------------------------------
# 3. ReLU Activation Function
# ------------------------------------------------------------
def relu(x):
    return np.maximum(0, x)

def main():

    # Accept input value
    value = float(input("Enter a value between -10 and 10: "))

    # Validate input
    if value < -10 or value > 10:
        print("Please enter a value between -10 and 10.")
        return

    # Create values from -10 to 10 for plotting
    x = np.linspace(-10, 10, 400)

    # Calculate activation functions
    sigmoid_values = sigmoid(x)
    tanh_values = tanh(x)
    relu_values = relu(x)

    # Calculate activation for entered value
    print("\nActivation Function Outputs")
    print("--------------------------------")

    print("Input Value :", value)
    print("Sigmoid     :", sigmoid(value))
    print("Tanh        :", tanh(value))
    print("ReLU        :", relu(value))


    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    plt.plot(x, sigmoid_values)
    plt.title("Sigmoid")
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.grid()

    plt.subplot(2, 3, 2)
    plt.plot(x, tanh_values)
    plt.title("Tanh")
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.grid()

    plt.subplot(2, 3, 3)
    plt.plot(x, relu_values)
    plt.title("ReLU")
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
