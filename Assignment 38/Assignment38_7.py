import pandas as pd
import matplotlib.pyplot as plt

border = "--"*40

#########################################
# Total number of students in the dataset
#########################################

print(border)
print("Load the dataset")
print(border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded succefully")
print("Initial entries from dataset are. : ")
print(df.head())

# Create a scatter plot of :
# StudyHours vs PreviousScore

plt.scatter(
        df['StudyHours'],
        df['PreviousScore'],
        s = 100,
        marker="o",
        alpha=0.8,
        edgecolors ="black",
        linewidths = 1,
        label  = "StudyHours vs PreviousScore"
    )

plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.grid(True)
plt.legend()
plt.show()

