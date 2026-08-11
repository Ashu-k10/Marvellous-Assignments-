import pandas as pd
import seaborn as sns
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

# Using pandas functions , Calculate and Display :
#    • Average StudyHours
#    • Average Attendance
#    • Maximum PreviousScore
#    • Minimum SleepHours

print(df[["StudyHours","Attendance","PreviousScore","SleepHours"]].describe())