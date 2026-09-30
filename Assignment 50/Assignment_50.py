import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

##############################
# Load the dataset 
##############################

data = load_breast_cancer()

x = pd.DataFrame(
    data.data,
    columns= data.feature_names
)

y = pd.Series(
    data.target,
    name="target"
)

print("Dataset loaded Sucessfully")
print("Number of Records :", x.shape[0])
print("Number of Features :",x.shape[1])

###############################
#Explore the Dataset
###############################

print("\n First 5 records :")
print(x.head())

print("\nDataset Information:")
print(x.info())

print("\nStatistical Summary :")
print(x.describe())

print("\nTarget Classes:")
print(data.target_names)

print("\nTarget Distribution :")
print(y.value_counts())

print("\nMissing Values:")
print(x.isnull().sum())

#################################
# EDA : Exploratory Data Analysis
#################################

sns.countplot(x=y)

plt.title("Distribution of tumor Classes")
plt.xlabel("Target Class")
plt.ylabel("Number of Samples")

plt.xticks(
    [0,1],
    ["Maligant","Benign"]
)

plt.show()

#######################
# Feature Co-relation
########################

correlation = x.corr()

sns.heatmap(
    correlation,
    cmap="coolwarm",
    annot=False
)

plt.title("Feature Correlation Heatmap")
plt.show()

###########################################
# Split Dataset into Training & Testing 
###########################################

x_train, x_test, y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training Data :",x_train.shape)
print("Testing Data :",x_test.shape)


##############################
# Feature Scaling 
##############################

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)

x_test = scaler.transform(x_test)

print("\nFeature Scaling Completed")

###################################
# Build Machine Learning Model
###################################

model = LogisticRegression(max_iter=1000)

model.fit(x_train,x_test)
print("Model Training Completed")

###################################
# Prediction ,Accuracy ,Confusion Matrix
###################################

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Malignant", "Benign"],
    yticklabels=["Malignant", "Benign"]
)

plt.xlabel("Predicted")s
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()

######################################
# Precision, Recall and F1-Score
######################################

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Malignant",
            "Benign"
        ]
    )
)
