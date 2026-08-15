import math

# Dataset
data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]

# Accept new student's data
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

# K value
K = 3

# Calculate Euclidean distance
distances = []

for hours, attend, result in data:

    distance = math.sqrt(
        (study_hours - hours) ** 2 +
        (attendance - attend) ** 2
    )

    distances.append((distance, result))

# Sort distances
distances.sort()

# Display distances
print("\nDistances:")

for distance, result in distances:
    print("Distance =", round(distance, 2), "Result =", result)

# Select K nearest neighbours
nearest = distances[:K]

print("\nK = 3 Nearest Neighbours:")

for distance, result in nearest:
    print("Distance =", round(distance, 2), "Result =", result)

# Majority voting
votes = {}

for distance, result in nearest:
    votes[result] = votes.get(result, 0) + 1

# Predict result
prediction = max(votes, key=votes.get)

print("\nVotes:", votes)
print("Predicted Result:", prediction)
