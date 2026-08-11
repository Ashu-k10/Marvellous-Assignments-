import pandas as pd
import matplotlib.pyplot as plt

def main():

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


# Plot a histogram of StudyHours.
# Explain what the distribution tell you.

plt.hist(
        df["StudyHours"],
        bins = 5,
        edgecolor = "Black"
)

plt.title("Distribution of Study Hours")
plt.xlabel("StudyHours")
plt.ylabel("Number of Students")

plt.show()

if __name__ == "__main__":
    main()

# Observation :
# The StudyHours values range from 1 to 8.5 hours.
# The distribution is fairly spread out, with students present across all study-hour ranges.
# The highest concentration is in the 7–8.5 hour range.
# The average study time is approximately 4.84 hours.
# Overall, the dataset contains students with low, moderate, and high study hours.



