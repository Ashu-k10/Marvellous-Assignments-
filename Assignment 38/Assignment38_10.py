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

# Plot SleepHours Against FinalResult.
# Does Sleeping more guarantee sucess ? Explain

pass_rate = df.groupby("SleepHours")["FinalResult"].mean() * 100

plt.bar(
    pass_rate.index,
    pass_rate.values,
    edgecolor= "Black"
)

plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("Pass Percentage (%)")

plt.show()