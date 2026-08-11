import pandas as pd 
import matplotlib.pyplot as plt

border = "-"*40

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

# Create a plot showing relationship between AssignmentsCompleted and FinalResult. Explain your Observation

pass_rate = df.groupby("AssignmentsCompleted")["FinalResult"].mean() * 100

plt.bar(pass_rate.index, pass_rate.values, edgecolor="black")

plt.xlabel("Assignments Completed")
plt.ylabel("Pass Percentage (%)")
plt.title("Assignments Completed vs Final Result")

plt.show()