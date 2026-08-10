import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler
import numpy as np

border = "-"*40

###################################
# Step 1 : Load the data
###################################

print(border)
print("Step 1 : Load the data")
print(border)

Dataset = "WinePredictor.csv"

df = pd.read_csv(Dataset)

print(border)
print("Dataset loaded Sucessfully ")
print(border)
print(df.head())

###################################
# Step 2 : Clean the dataset 
###################################

print(border)
print("Step 2 : Clean the dataset")
print(border)

df.dropna(inplace=True)

print("Shape of Data :",df.shape[0])
print("Total Records : ",df.shape[0])
print("Total Columns :",df.shape[1])
    
print(border)

######################################################
# Step 3 : Seperate Independent & Dependent Varibles
######################################################

print(border)
print("Step 3 : Seperate Independent & Dependent Varibles")
print(border)

X = df.drop(columns=['Class'])
Y = df['Class']

print("Shape of X :",X.shape)
print("Shape of Y :",Y.shape)

print(border)
print("Input columns :",X.columns.tolist())
print("Output column : Class")
print(border)

#######################################################
# Step 4 : Split the dataset for training and testing 
#######################################################

print(border)
print("Step 4 : Split the dataset for training and testing")
print(border)
    
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify= Y)

print(border)
print("Details in training and testing the data")
print("Shape of X_train : ",X_train.shape)
print("Shape of X_test : ",X_test.shape)

print("Shape of Y_train : ",Y_train.shape)
print("Shape of Y_test : ",Y_test.shape)

################################
# Step 5 : Features scaling  
################################

print(border)
print("Step 5 : Features scaling")
print(border)

scalar = StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

print("Feature Scaling done")

################################
# Step 6 : Build the model  
################################

print(border)
print("Step 5 : Build the model  ")
print(border)

model = KNeighborsClassifier(n_neighbors=5)

print("Classification model is Created ")

################################
# Step 7 : Train the model  
################################

print(border)
print(" Step 7 : Train the model  ")
print(border)

model = model.fit(X_train_scaled, Y_train)

print("Model trained successfully")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test, Y_pred)

print("Model accuracy is :", accuracy * 100)

