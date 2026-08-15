import math

# Dataset
# Study Hours, Attendance, Result
data = [
    (1, 50, "Fail"),
    (2, 55, "Fail"),
    (2, 60, "Fail"),
    (3, 65, "Pass"),
    (4, 70, "Pass"),
    (5, 75, "Pass"),
    (6, 80, "Pass"),
    (7, 85, "Pass")
]

# Accept new student's data
study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))

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

# Select K nearest neighbours
nearest = distances[:K]

print("\nK Nearest Neighbours:")

for distance, result in nearest:
    print("Distance =", round(distance, 2), "Result =", result)


# Predict result
prediction = max(votes, key=votes.get)

print("Predicted Result:", prediction)
