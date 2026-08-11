import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

#Count how many students Passed (FinalResult = 1)
print(df[df["FinalResult"] == 1].shape[0])

#Count how many students Passed (FinalResult = 0)
print(df[df["FinalResult"] == 0].shape[0])








