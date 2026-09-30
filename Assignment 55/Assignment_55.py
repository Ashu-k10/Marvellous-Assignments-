import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

###########################################
# Step 1 : load the dataset
############################################

df = pd.read_csv('Customer_Loan_Approval.csv')

print("Shape of dataset : ",df.shape)
print("First few Records :")
print(df.head())

###########################################
# Step 2 : Check for Missing Values
############################################

print("\nMissing Values :")
print(df.isnull().sum())

#If missing Values exists, Remove them
df = df.dropna()

##########################################
# Step 3 : Seperate features and labels
##########################################

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]


print("\nInput Variables:")
print(X.head())

print("\nOutput Variable:")
print(Y.head())

###################################################
# Step 4. Split Dataset into Training and Testing Data
###################################################

X_Train , X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

#############################
# Step 5 : Create Models
#############################

#Logistic Regression
Logistic_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

#Decision Tree
decision_tree_model = DecisionTreeClassifier(
    random_state=42
)

## KNN
knn_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", KNeighborsClassifier(n_neighbors=5))
])

##################################
# 6. Train Logistic Regression 
#################################

Logistic_model.fit(X_Train, Y_train)

Y_pred_lr = Logistic_model.predict(X_test)

accuracy_lr = accuracy_score(Y_test, Y_pred_lr)

print("\nLogistic Regression Accuracy:",
      accuracy_lr)

#####################################
# 7. Train Decision Tree
#####################################

decision_tree_model.fit(X_Train, Y_train)

Y_pred_dt = decision_tree_model.predict(X_test)

accuracy_dt = accuracy_score(Y_test, Y_pred_dt)

print("Decision Tree Accuracy:",
      accuracy_dt)

#####################################
# 8. Train KNN
#####################################

knn_model.fit(X_Train, Y_train)

Y_pred_knn = knn_model.predict(X_test)

accuracy_knn = accuracy_score(Y_test, Y_pred_knn)

print("KNN Accuracy:",
      accuracy_knn)

#######################################
# 9. Create Hard Voting Classifier
#######################################

hard_voting = VotingClassifier(
    estimators=[
        ("lr", Logistic_model),
        ("dt", decision_tree_model),
        ("knn", knn_model)
    ],
    voting="hard"
)

# Train Hard Voting Classifier
hard_voting.fit(X_Train, Y_train)

Y_pred_hard = hard_voting.predict(X_test)

accuracy_hard = accuracy_score(
    Y_test,
    Y_pred_hard
)

print("Hard Voting Accuracy:",
      accuracy_hard)

#######################################
# 10. Create Soft Voting Classifier
#######################################

soft_voting = VotingClassifier(
    estimators=[
        ("lr", Logistic_model),
        ("dt", decision_tree_model),
        ("knn", knn_model)
    ],
    voting="soft"
)


# Train Soft Voting Classifier
soft_voting.fit(X_Train, Y_train)

Y_pred_soft = soft_voting.predict(X_test)

accuracy_soft = accuracy_score(
    Y_test,
    Y_pred_soft
)

print("Soft Voting Accuracy:",
      accuracy_soft)

#######################################
# 11.  Compare All Models
#######################################


results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],

    "Accuracy": [
        accuracy_lr,
        accuracy_dt,
        accuracy_knn,
        accuracy_hard,
        accuracy_soft
    ]
})


print("\n==============================")
print("       MODEL COMPARISON")
print("==============================")

print(results)

#################################
# 12. Accuracy in Percentage
#################################

results["Accuracy (%)"] = results["Accuracy"] * 100

print("\nAccuracy in Percentage:")
print(results)


###########################
# 13. Final Comparison
###########################

print("\n==============================")
print("       FINAL COMPARISON")
print("==============================")

for index, row in results.iterrows():

    print(
        row["Model"],
        "->",
        round(row["Accuracy (%)"], 2),
        "%"
    )
