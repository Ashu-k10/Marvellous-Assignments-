import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


# ============================================================
# 1. LOAD DATASET
# ============================================================

BORDER = "_" * 50

print(BORDER)
print("        STUDENT PERFORMANCE - DECISION TREE")
print(BORDER)

DATA_PATH = "student_performance_ml.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset loaded successfully!")
print("\nFirst 5 records:")
print(df.head())


# ============================================================
# 2. SEPARATE FEATURES AND TARGET
# ============================================================

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]


# ============================================================
# 3. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)


# ============================================================
# 4. TRAIN ORIGINAL DECISION TREE MODEL
# ============================================================

print("\n" + BORDER)
print("4. TRAINING ORIGINAL DECISION TREE")
print(BORDER)

model_full = DecisionTreeClassifier(random_state=42)

model_full.fit(X_train, Y_train)

print("Model trained successfully!")


# ============================================================
# 5. PREDICT AND CALCULATE ORIGINAL ACCURACY
# ============================================================

Y_pred = model_full.predict(X_test)

original_accuracy = accuracy_score(Y_test, Y_pred)

print("\nOriginal Model Accuracy:",
      original_accuracy * 100, "%")


# ============================================================
# 6. FEATURE IMPORTANCE
# ============================================================

print("\n" + BORDER)
print("6. FEATURE IMPORTANCE")
print(BORDER)

importance = model_full.feature_importances_

for feature, score in zip(X.columns, importance):
    print(f"{feature:20} : {score:.4f}")


most_important = X.columns[importance.argmax()]
least_important = X.columns[importance.argmin()]

print("\nMost Important Feature :", most_important)
print("Least Important Feature:", least_important)


# ============================================================
# 7. REMOVE SLEEPHOURS
# ============================================================

print("\n" + BORDER)
print("7. REMOVE SLEEPHOURS")
print(BORDER)

X_without_sleep = df.drop(
    columns=["FinalResult", "SleepHours"]
)

Y_without_sleep = df["FinalResult"]


X_train_sleep, X_test_sleep, Y_train_sleep, Y_test_sleep = train_test_split(
    X_without_sleep,
    Y_without_sleep,
    test_size=0.2,
    random_state=42
)


model_without_sleep = DecisionTreeClassifier(
    random_state=42
)

model_without_sleep.fit(
    X_train_sleep,
    Y_train_sleep
)


Y_pred_without_sleep = model_without_sleep.predict(
    X_test_sleep
)


accuracy_without_sleep = accuracy_score(
    Y_test_sleep,
    Y_pred_without_sleep
)


print("Previous Accuracy:",
      original_accuracy * 100, "%")

print("New Accuracy:",
      accuracy_without_sleep * 100, "%")


if accuracy_without_sleep > original_accuracy:
    print("Removing SleepHours improved performance.")

elif accuracy_without_sleep < original_accuracy:
    print("Removing SleepHours reduced performance.")

else:
    print("Removing SleepHours did not affect performance.")


# ============================================================
# 8. MODEL USING ONLY STUDYHOURS AND ATTENDANCE
# ============================================================

print("\n" + BORDER)
print("8. MODEL USING ONLY STUDYHOURS + ATTENDANCE")
print(BORDER)

X_two = df[
    ["StudyHours", "Attendance"]
]

Y_two = df["FinalResult"]


X_train_two, X_test_two, Y_train_two, Y_test_two = train_test_split(
    X_two,
    Y_two,
    test_size=0.2,
    random_state=42
)


model_two_features = DecisionTreeClassifier(
    random_state=42
)

model_two_features.fit(
    X_train_two,
    Y_train_two
)


Y_pred_two = model_two_features.predict(
    X_test_two
)


accuracy_two_features = accuracy_score(
    Y_test_two,
    Y_pred_two
)


print("Full Feature Accuracy:",
      original_accuracy * 100, "%")

print("Two Feature Accuracy:",
      accuracy_two_features * 100, "%")


if accuracy_two_features >= original_accuracy:
    print("The two-feature model is still performing well.")

else:
    print("The two-feature model has lower performance.")


# ============================================================
# 9. PREDICT RESULTS FOR 5 NEW STUDENTS
# ============================================================

print("\n" + BORDER)
print("9. PREDICTIONS FOR NEW STUDENTS")
print(BORDER)

new_students = pd.DataFrame({
    "StudyHours": [5, 2, 7, 3, 6],
    "Attendance": [85, 60, 95, 70, 90],
    "PreviousScore": [75, 50, 88, 55, 80],
    "SleepHours": [7, 6, 8, 5, 7]
})


predictions = model_full.predict(new_students)

new_students["PredictedResult"] = predictions


print("\nNew Students:")
print(new_students)


print("\nPrediction Results:")
print("-------------------")

for index, row in new_students.iterrows():

    result = "Pass" if row["PredictedResult"] == 1 else "Fail"

    print(
        f"Student {index + 1}: "
        f"StudyHours={row['StudyHours']}, "
        f"Attendance={row['Attendance']}%, "
        f"PreviousScore={row['PreviousScore']}, "
        f"SleepHours={row['SleepHours']} "
        f"--> {result}"
    )


# ============================================================
# 10. MANUAL ACCURACY CALCULATION
# ============================================================

print("\n" + BORDER)
print("10. MANUAL ACCURACY CALCULATION")
print(BORDER)

correct_predictions = 0

for actual, predicted in zip(Y_test, Y_pred):

    if actual == predicted:
        correct_predictions += 1


total_predictions = len(Y_test)

manual_accuracy = (
    correct_predictions / total_predictions
)


print("Correct Predictions:",
      correct_predictions)

print("Total Predictions:",
      total_predictions)

print("Manual Accuracy:",
      manual_accuracy * 100, "%")


print("Sklearn Accuracy:",
      original_accuracy * 100, "%")


if manual_accuracy == original_accuracy:
    print("Both accuracies are the same.")

else:
    print("The accuracies are different.")


# ============================================================
# 11. FIND MISCLASSIFIED STUDENTS
# ============================================================

print("\n" + BORDER)
print("11. MISCLASSIFIED STUDENTS")
print(BORDER)

misclassified = X_test.copy()

misclassified["ActualResult"] = Y_test
misclassified["PredictedResult"] = Y_pred


misclassified = misclassified[
    misclassified["ActualResult"]
    != misclassified["PredictedResult"]
]


print("\nMisclassified Students:")

if len(misclassified) > 0:
    print(misclassified)

else:
    print("No students were misclassified.")


print(
    "\nNumber of Misclassified Students:",
    len(misclassified)
)


print("\nCommon Pattern:")
print(
    "Misclassified students may have borderline "
    "values in StudyHours, Attendance, or PreviousScore."
)
print(
    "Check the displayed rows to identify the actual "
    "pattern in the dataset."
)


# ============================================================
# 12. DECISION TREE VISUALIZATION
# ============================================================

print("\n" + BORDER)
print("12. DECISION TREE VISUALIZATION")
print(BORDER)

plt.figure(figsize=(18, 10))

plot_tree(
    model_full,
    feature_names=X.columns,
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True
)

plt.title("Student Performance Decision Tree")

plt.show()


# ============================================================
# 13. CREATE PERFORMANCE INDEX
# ============================================================

print("\n" + BORDER)
print("13. PERFORMANCE INDEX")
print(BORDER)

df_performance = df.copy()

df_performance["PerformanceIndex"] = (
    df_performance["StudyHours"] * 2
) + df_performance["Attendance"]


X_performance = df_performance.drop(
    "FinalResult",
    axis=1
)

Y_performance = df_performance["FinalResult"]


X_train_performance, X_test_performance, \
Y_train_performance, Y_test_performance = train_test_split(
    X_performance,
    Y_performance,
    test_size=0.2,
    random_state=42
)


model_performance = DecisionTreeClassifier(
    random_state=42
)

model_performance.fit(
    X_train_performance,
    Y_train_performance
)


Y_pred_performance = model_performance.predict(
    X_test_performance
)


accuracy_performance = accuracy_score(
    Y_test_performance,
    Y_pred_performance
)


print("Original Accuracy:",
      original_accuracy * 100, "%")

print("PerformanceIndex Accuracy:",
      accuracy_performance * 100, "%")


if accuracy_performance > original_accuracy:
    print("Accuracy improved after adding PerformanceIndex.")

elif accuracy_performance < original_accuracy:
    print("Accuracy decreased after adding PerformanceIndex.")

else:
    print("Accuracy remained the same.")


# ============================================================
# 14. DECISION TREE WITH max_depth = None
# ============================================================

print("\n" + BORDER)
print("14. DECISION TREE WITH max_depth=None")
print(BORDER)

model_unlimited = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)


model_unlimited.fit(
    X_train,
    Y_train
)


# Training predictions
Y_train_pred = model_unlimited.predict(
    X_train
)


# Testing predictions
Y_test_pred = model_unlimited.predict(
    X_test
)


# Training accuracy
training_accuracy = accuracy_score(
    Y_train,
    Y_train_pred
)


# Testing accuracy
testing_accuracy = accuracy_score(
    Y_test,
    Y_test_pred
)


print("Training Accuracy:",
      training_accuracy * 100, "%")

print("Testing Accuracy:",
      testing_accuracy * 100, "%")


# ============================================================
# 15. OVERFITTING CHECK
# ============================================================

print("\n" + BORDER)
print("15. OVERFITTING CHECK")
print(BORDER)

if training_accuracy == 1.0 and testing_accuracy < 1.0:

    print("The model is likely overfitting.")

    print(
        "The Decision Tree has learned the training data "
        "too closely, including specific patterns or noise."
    )

    print(
        "As a result, it achieves very high training accuracy "
        "but performs worse on unseen testing data."
    )

else:

    print(
        "The model does not show the specific "
        "100% training accuracy vs lower testing "
        "accuracy pattern."
    )


# ============================================================
# END
# ============================================================

print("\n" + BORDER)
print("ALL EXPERIMENTS COMPLETED")
print(BORDER)
