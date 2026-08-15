import math

data = [
    (1,2,"Red"),
    (2,3,"Red"),
    (3,1,"Blue"),
    (6,5,"Blue")
]

# Step 1: Accept X and Y coordinates of new point
x = float(input("Enter X Coordinate : "))
y = float(input("Enter Y coordinate : "))

new_point = (x ,y)
K = 3


# Step 2: Compute Euclidean distance
distances = []

for point_x , point_y , label in data :
    distance = math.sqrt(
        (x - point_x) ** 2 + 
        (y - point_y) ** 2
    )

    distances.append((distance, label))

# Step 3: Sort the distances
distances.sort()

print("\nDistances:")
for distance, label in distances:
    print("Distance =", round(distance, 2), "Label =", label)


# Step 4: Select K = 3 nearest neighbours
nearest = distances[:K]

print("\n3 Nearest Neighbours:")
for distance, label in nearest:
    print("Distance =", round(distance, 2), "Label =", label)


# Step 5: Predict class using majority voting
votes = {}

for distance, label in nearest:
    votes[label] = votes.get(label, 0) + 1

predicted_class = max(votes, key=votes.get)

print("Predicted Class:", predicted_class)

