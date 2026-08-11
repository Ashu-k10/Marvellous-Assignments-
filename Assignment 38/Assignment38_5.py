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

# Based on the dataset values, analyse whether:
# • Higher StudyHours increase the chance of passing
# • Higher Attendence improves FinalResult
#   Write your Observation in 4-5 lines
# ==>
# 1. Students who passed had an average StudyHours of about 6.37 hours, compared to 2.55 hours for failed students.
# 2. Higher StudyHours clearly show a higher chance of passing in this dataset.
# 3. Passed students had an average Attendance of about 86.61%, while failed students averaged 67.75%.
# 4. Students with attendance above 80% all passed, indicating that higher attendance strongly improves the chance of passing.
# 5. Overall, both StudyHours and Attendance have a positive relationship with FinalResult.