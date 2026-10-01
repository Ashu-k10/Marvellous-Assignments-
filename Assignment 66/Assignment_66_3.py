import math

# ------------------------------------------------------------
# Mean Squared Error
# ------------------------------------------------------------

def mean_squared_error(actual, predicted):
    total = 0

    for i in range(len(actual)):
        error = actual[i] - predicted[i]
        total = total + (error ** 2)

    return total / len(actual)


# ------------------------------------------------------------
# Binary Cross Entropy
# ------------------------------------------------------------

def binary_cross_entropy(actual, predicted):
    total = 0

    for i in range(len(actual)):
        # Avoid log(0)
        p = max(min(predicted[i], 1 - 1e-15), 1e-15)

        loss = -(actual[i] * math.log(p) +
                 (1 - actual[i]) * math.log(1 - p))

        total = total + loss

    return total / len(actual)


# Actual values
actual = [1, 0, 1, 1]

# Predicted values
predicted = [0.9, 0.2, 0.8, 0.7]

# Calculate losses
mse = mean_squared_error(actual, predicted)
bce = binary_cross_entropy(actual, predicted)

# Display results
print("Actual Values    :", actual)
print("Predicted Values :", predicted)

print("\nMean Squared Error (MSE) :", mse)
print("Binary Cross Entropy (BCE) :", bce)
