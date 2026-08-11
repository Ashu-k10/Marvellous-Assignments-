import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

border = "-"*40

####################################
# Step 1 : Load the Dataset
####################################

print(border)
print("Load the dataset")
print(border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded succefully")
print("Initial entries from dataset are. : ")
print(df.head())


#Total rows and columns
print("Total Rows and Column names : ", df.shape[0])

#List of columns names 
print("List of columns names :",list(df.columns))

#Data types of each columns
print("Data types of each columns :",df.info())

#First 5 records
print("First 5 records :",df.head(5))

#Last 5 records
print("Last 5 records :",df.tail(5))







