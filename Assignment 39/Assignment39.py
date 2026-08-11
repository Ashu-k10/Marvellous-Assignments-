import pandas as pd
import matplotlib.pyplot as PythonFinalizationError
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
)

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


# Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit()

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train,Y_train)
print("Model Trained Sucessfully")

# Use the trained model to predict results for X_test.
# Display predicted values among with actual values

Y_pred = model.predict(X_test)
print("Predicted Values:", Y_pred)
print("Actual Values:   ", Y_test.values)

# Calculate model accuracy using accuracy_score.
# Display the result in percentage format.

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of model is : ",accuracy*100)

# Generate confusion matrix using sklearn
# Display it using ConfusionMatrixDisplay
#  Explain clearly : TN,TP,FN,FP

print("Confustion matrix")
cm = confusion_matrix(Y_test, Y_pred)
print(cm)

# Train three Decision Tree models with :
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
#    max_depth = 1
model = DecisionTreeClassifier(max_depth=1)
model.fit(X_train,Y_train)
print("Model with max_depth 1 Trained Sucessfully")

#    max_depth = 3
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train,Y_train)
print("Model with max_depth 3 Trained Sucessfully")

#    max_depth = None
model = DecisionTreeClassifier(max_depth=0)
model.fit(X_train,Y_train)
print("Model with max_depth 0 Trained Sucessfully")












