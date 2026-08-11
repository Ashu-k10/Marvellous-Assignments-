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


# Use value_counts() to analyze the distribution of FinalResult.Calculate the percentage of Pass and Fail Students.
# Is the dataset balanced ? Justify your Answer

result_counts = df["FinalResult"].value_counts()

print(result_counts)

result_percentage = df['FinalResult'].value_counts(normalize=True) * 100
print(result_percentage)







