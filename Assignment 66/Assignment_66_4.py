# Take input values

x = float(input("Enter input: "))
weight = float(input("Enter weight: "))
bias = float(input("Enter bias: "))
target = float(input("Enter target output: "))
learning_rate = float(input("Enter learning rate: "))

# ------------------------------------------------------------
# Step 1: Calculate prediction
# ------------------------------------------------------------

prediction = (x * weight) + bias

# ------------------------------------------------------------
# Step 2: Calculate error
# ------------------------------------------------------------

error = target - prediction

# Store old weight
old_weight = weight

# ------------------------------------------------------------
# Step 3: Calculate gradient
# ------------------------------------------------------------

gradient = error * x

# ------------------------------------------------------------
# Step 4: Update weight
# ------------------------------------------------------------

weight = weight + (learning_rate * gradient)

# ------------------------------------------------------------
# Display results
# ------------------------------------------------------------

print("\n----- ANN Weight Update -----")

print("Input       :", x)
print("Old Weight  :", old_weight)
print("Bias        :", bias)
print("Target      :", target)
print("Prediction  :", prediction)
print("Error       :", error)
print("Gradient    :", gradient)
print("Learning Rate:", learning_rate)

print("Updated Weight :", weight)
