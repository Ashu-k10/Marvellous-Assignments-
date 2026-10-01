# ============================================================
# Deep Learning Assignment
# Loan Default Prediction using Multi-Layer Perceptron
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("loan_default.csv")

print("\n================ DATASET INFORMATION ================\n")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# ============================================================
# 2. EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n================ EXPLORATORY DATA ANALYSIS ================\n")

print("Column Names:")
print(df.columns)

print("\nUnique Values:")
for column in df.columns:
    print(column, ":", df[column].unique())

# ============================================================
# 3. CHECK MISSING VALUES
# ============================================================

print("\n================ MISSING VALUES ================\n")

print(df.isnull().sum())

# Fill missing numerical values using median
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values using mode
categorical_columns = df.select_dtypes(include=["object"]).columns

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing values after treatment:")
print(df.isnull().sum())

# ============================================================
# 4. CHECK TARGET CLASS BALANCE
# ============================================================

print("\n================ TARGET CLASS DISTRIBUTION ================\n")

print(df["Default"].value_counts())

print("\nTarget Percentage:")
print(df["Default"].value_counts(normalize=True) * 100)

# Plot target distribution
df["Default"].value_counts().plot(
    kind="bar",
    title="Loan Default Class Distribution"
)

plt.xlabel("Default Class")
plt.ylabel("Number of Applicants")
plt.tight_layout()
plt.show()

# ============================================================
# 5. ENCODE CATEGORICAL VARIABLES
# ============================================================

print("\n================ ENCODING CATEGORICAL VARIABLES ================\n")

# Encode PreviousDefault
if df["PreviousDefault"].dtype == "object":
    df["PreviousDefault"] = df["PreviousDefault"].map({
        "Yes": 1,
        "No": 0
    })

# Encode HomeOwnership using one-hot encoding
df = pd.get_dummies(
    df,
    columns=["HomeOwnership"],
    drop_first=True
)

print("Dataset after encoding:")
print(df.head())

# ============================================================
# 6. SEPARATE X AND y
# ============================================================

X = df.drop("Default", axis=1)
y = df["Default"]

print("\n================ X AND y ================\n")

print("X shape:", X.shape)
print("y shape:", y.shape)

# ============================================================
# 7. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n================ TRAIN TEST SPLIT ================\n")

print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])

# ============================================================
# 8. FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed.")

# ============================================================
# 9. CREATE MLP CLASSIFIER
# ============================================================

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

# ============================================================
# 10. TRAIN MODEL
# ============================================================

print("\n================ MODEL TRAINING ================\n")

model.fit(X_train_scaled, y_train)

print("Model training completed.")

# ============================================================
# 11. PREDICTION
# ============================================================

y_pred = model.predict(X_test_scaled)

# ============================================================
# 12. ACCURACY
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n================ MODEL ACCURACY ================\n")

print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")

# ============================================================
# 13. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(y_test, y_pred)

print("\n================ CONFUSION MATRIX ================\n")

print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Low Risk", "High Risk"]
)

disp.plot()
plt.title("Loan Default Confusion Matrix")
plt.tight_layout()
plt.show()

# ============================================================
# 14. CLASSIFICATION REPORT
# ============================================================

print("\n================ CLASSIFICATION REPORT ================\n")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Low Risk", "High Risk"]
    )
)

# ============================================================
# 15. PRECISION, RECALL AND F1 SCORE
# ============================================================

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

print("\n================ PERFORMANCE METRICS ================\n")

print("Precision:", precision)
print("Recall   :", recall)
print("F1-Score :", f1)

# ============================================================
# 16. PLOT TRAINING LOSS
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    model.loss_curve_,
    label="Training Loss"
)

plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# ============================================================
# 17. TEST MODEL ON NEW LOAN APPLICANT
# ============================================================

print("\n================ NEW APPLICANT PREDICTION ================\n")

# Example applicant
new_applicant = pd.DataFrame({
    "Age": [35],
    "Income": [650000],
    "LoanAmount": [250000],
    "CreditScore": [720],
    "EmploymentYears": [8],
    "ExistingLoans": [1],
    "MonthlyDebt": [15000],
    "LoanTerm": [60],
    "PreviousDefault": [0],
    "HomeOwnership_Own": [1],
    "HomeOwnership_Rent": [0]
})

# Make sure columns are in the same order
new_applicant = new_applicant.reindex(
    columns=X.columns,
    fill_value=0
)

# Scale new applicant
new_applicant_scaled = scaler.transform(new_applicant)

# Prediction
new_prediction = model.predict(new_applicant_scaled)

# Probability
new_probability = model.predict_proba(new_applicant_scaled)

print("Prediction:", new_prediction[0])

print(
    "Default Probability:",
    new_probability[0][1]
)

if new_prediction[0] == 0:
    print("Result: LOW DEFAULT RISK")
else:
    print("Result: HIGH DEFAULT RISK")


# ============================================================
# HYPERPARAMETER EXPERIMENTS
# ============================================================

print("\n\n============================================================")
print("              HYPERPARAMETER EXPERIMENTS")
print("============================================================")

# ============================================================
# EXPERIMENT 1 - ACTIVATION FUNCTION
# ============================================================

print("\n================ EXPERIMENT 1: ACTIVATION ================\n")

activations = [
    "identity",
    "logistic",
    "tanh",
    "relu"
]

activation_results = []

for activation in activations:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=activation,
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(
        X_train_scaled,
        y_train
    )

    prediction = experiment_model.predict(
        X_test_scaled
    )

    accuracy_value = accuracy_score(
        y_test,
        prediction
    )

    activation_results.append(
        [activation, accuracy_value]
    )

activation_df = pd.DataFrame(
    activation_results,
    columns=["Activation", "Accuracy"]
)

print(activation_df)

# ============================================================
# EXPERIMENT 2 - HIDDEN LAYERS
# ============================================================

print("\n================ EXPERIMENT 2: HIDDEN LAYERS ================\n")

hidden_layers = [
    (10,),
    (20, 10),
    (50, 25),
    (100, 50, 25)
]

hidden_results = []

for layers in hidden_layers:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=layers,
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(
        X_train_scaled,
        y_train
    )

    prediction = experiment_model.predict(
        X_test_scaled
    )

    accuracy_value = accuracy_score(
        y_test,
        prediction
    )

    hidden_results.append(
        [str(layers), accuracy_value]
    )

hidden_df = pd.DataFrame(
    hidden_results,
    columns=["Hidden Layers", "Accuracy"]
)

print(hidden_df)

# ============================================================
# EXPERIMENT 3 - LEARNING RATE
# ============================================================

print("\n================ EXPERIMENT 3: LEARNING RATE ================\n")

learning_rates = [
    0.0001,
    0.001,
    0.01,
    0.1
]

learning_results = []

for learning_rate in learning_rates:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        learning_rate_init=learning_rate,
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(
        X_train_scaled,
        y_train
    )

    prediction = experiment_model.predict(
        X_test_scaled
    )

    accuracy_value = accuracy_score(
        y_test,
        prediction
    )

    learning_results.append(
        [learning_rate, accuracy_value]
    )

learning_df = pd.DataFrame(
    learning_results,
    columns=["Learning Rate", "Accuracy"]
)

print(learning_df)

# ============================================================
# HYPERPARAMETER COMPARISON
# ============================================================

print("\n============================================================")
print("                 EXPERIMENT SUMMARY")
print("============================================================")

print("\nActivation Function Results:")
print(activation_df)

print("\nHidden Layer Results:")
print(hidden_df)

print("\nLearning Rate Results:")
print(learning_df)

# ============================================================
# END
# ============================================================

print("\n============================================================")
print("             LOAN DEFAULT PREDICTION COMPLETED")
print("============================================================")
