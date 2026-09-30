# ============================================================
# Machine Learning Assignment
# Fraudulent Transaction Detection
#
# Models:
# 1. Decision Tree
# 2. Bagging Classifier
# 3. Random Forest
# 4. AdaBoost Classifier
# 5. Voting Classifier
#
# Evaluation:
# Accuracy, Precision, Recall, F1 Score, Confusion Matrix
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ============================================================
# 1. Load Dataset
# ============================================================

df = pd.read_csv("fraudulent_transactions.csv")

print("\nDataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 2. Remove Missing Values
# ============================================================

df = df.dropna()

print("\nShape after removing missing values:")
print(df.shape)


# ============================================================
# 3. Encode Categorical Columns
# ============================================================

# Device Type is categorical
# Example:
# Mobile, Desktop, Tablet

label_encoder = LabelEncoder()

if "Device Type" in df.columns:
    df["Device Type"] = label_encoder.fit_transform(
        df["Device Type"]
    )


# ============================================================
# 4. Convert Transaction Time
# ============================================================

# If Transaction Time is stored as text/time,
# convert it into useful numerical information.

if "Transaction Time" in df.columns:

    try:
        time_data = pd.to_datetime(
            df["Transaction Time"]
        )

        df["Transaction_Hour"] = time_data.dt.hour
        df["Transaction_Minute"] = time_data.dt.minute

        df.drop(
            "Transaction Time",
            axis=1,
            inplace=True
        )

    except:
        print("Transaction Time could not be converted.")


# ============================================================
# 5. Separate Features and Target
# ============================================================

X = df.drop("Fraud", axis=1)

y = df["Fraud"]


print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())


# ============================================================
# 6. Train-Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# ============================================================
# 7. Create Models
# ============================================================

# ------------------------------------------------------------
# Model 1: Decision Tree
# ------------------------------------------------------------

decision_tree = DecisionTreeClassifier(
    random_state=42,
    class_weight="balanced"
)


# ------------------------------------------------------------
# Model 2: Bagging Classifier
# ------------------------------------------------------------

bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(
        class_weight="balanced"
    ),
    n_estimators=100,
    random_state=42
)


# ------------------------------------------------------------
# Model 3: Random Forest
# ------------------------------------------------------------

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)


# ------------------------------------------------------------
# Model 4: AdaBoost
# ------------------------------------------------------------

adaboost = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(
        max_depth=1
    ),
    n_estimators=100,
    learning_rate=0.5,
    random_state=42
)


# ------------------------------------------------------------
# Model 5: Voting Classifier
# ------------------------------------------------------------

voting = VotingClassifier(
    estimators=[
        (
            "decision_tree",
            DecisionTreeClassifier(
                max_depth=5,
                random_state=42,
                class_weight="balanced"
            )
        ),
        (
            "random_forest",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                class_weight="balanced"
            )
        ),
        (
            "logistic_regression",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced"
            )
        )
    ],
    voting="hard"
)


# ============================================================
# 8. Store Models
# ============================================================

models = {
    "Decision Tree": decision_tree,
    "Bagging": bagging,
    "Random Forest": random_forest,
    "AdaBoost": adaboost,
    "Voting": voting
}


# ============================================================
# 9. Train and Evaluate Models
# ============================================================

results = []


for name, model in models.items():

    print("\n")
    print("=" * 60)
    print(name)
    print("=" * 60)

    # Train
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    # Store results
    results.append({
        "Algorithm": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })


    # --------------------------------------------------------
    # Print Metrics
    # --------------------------------------------------------

    print("\nAccuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))


    # --------------------------------------------------------
    # Classification Report
    # --------------------------------------------------------

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            zero_division=0
        )
    )


    # --------------------------------------------------------
    # Confusion Matrix
    # --------------------------------------------------------

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    print("Confusion Matrix:")
    print(cm)


    # --------------------------------------------------------
    # Plot Confusion Matrix
    # --------------------------------------------------------

    plt.figure(figsize=(5, 4))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Normal", "Fraud"],
        yticklabels=["Normal", "Fraud"]
    )

    plt.title(
        name + " - Confusion Matrix"
    )

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.tight_layout()

    plt.show()


# ============================================================
# 10. Final Comparison Table
# ============================================================

results_df = pd.DataFrame(results)

print("\n")
print("=" * 80)
print("FINAL MODEL COMPARISON")
print("=" * 80)

print(
    results_df.to_string(
        index=False
    )
)


# ============================================================
# 11. Display Results in Percentage
# ============================================================

percentage_results = results_df.copy()

for column in [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score"
]:
    percentage_results[column] = (
        percentage_results[column] * 100
    ).round(2)


print("\n")
print("=" * 80)
print("FINAL COMPARISON IN PERCENTAGE")
print("=" * 80)

print(
    percentage_results.to_string(
        index=False
    )
)


# ============================================================
# 12. Comparison Graph
# ============================================================

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score"
]

percentage_results.set_index(
    "Algorithm"
)[metrics].plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title(
    "Comparison of Fraud Detection Models"
)

plt.xlabel("Algorithm")

plt.ylabel("Score (%)")

plt.xticks(
    rotation=20
)

plt.legend(
    loc="lower right"
)

plt.tight_layout()

plt.show()


# ============================================================
# 13. Find Model with Highest F1 Score
# ============================================================

best_index = results_df[
    "F1 Score"
].idxmax()

best_model = results_df.loc[
    best_index
]

print("\n")
print("=" * 60)
print("MODEL WITH HIGHEST F1 SCORE")
print("=" * 60)

print(
    best_model
)
