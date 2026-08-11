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

# Draw a boxplot for Attendence. Identify if any outliers are present
 
plt.boxplot(
        df["Attendance"],
    )

plt.title("Attendance")
plt.xlabel("Student")
plt.ylabel("Total Attendence")

plt.show()