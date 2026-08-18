import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


def marvellous_classifier(data_path):

    border = "-" * 50

    # --------------------------------------------------
    # Step 1: Load Dataset
    # --------------------------------------------------

    print(border)
    print("Step 1: Load Dataset")
    print(border)

    df = pd.read_csv(data_path)

    # Remove unwanted spaces from column names
    df.columns = df.columns.str.strip()

    print("First 5 records:")
    print(df.head())

    print("\nColumn Names:")
    print(df.columns.tolist())


    # --------------------------------------------------
    # Step 2: Clean Dataset
    # --------------------------------------------------

    print("\n" + border)
    print("Step 2: Clean Dataset")
    print(border)

    df.dropna(inplace=True)

    print("Total Records :", df.shape[0])
    print("Total Columns :", df.shape[1])


    # --------------------------------------------------
    # Step 3: Separate Input and Output
    # --------------------------------------------------

    print("\n" + border)
    print("Step 3: Separate Input and Output")
    print(border)

    # Target column
    target = "Class"

    # Check whether target column exists
    if target not in df.columns:
        print("\nError: 'Class' column not found.")
        print("Available columns are:", df.columns.tolist())
        return

    X = df.drop(columns=[target])
    Y = df[target]

    print("Input columns :", X.columns.tolist())
    print("Output column :", target)

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)


    # --------------------------------------------------
    # Step 4: Split Dataset
    # --------------------------------------------------

    print("\n" + border)
    print("Step 4: Split Dataset")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("X_train :", X_train.shape)
    print("X_test  :", X_test.shape)
    print("Y_train :", Y_train.shape)
    print("Y_test  :", Y_test.shape)


    # --------------------------------------------------
    # Step 5: Feature Scaling
    # --------------------------------------------------

    print("\n" + border)
    print("Step 5: Feature Scaling")
    print(border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Feature scaling completed.")


    # --------------------------------------------------
    # Step 6: Create KNN Model
    # --------------------------------------------------

    print("\n" + border)
    print("Step 6: Build KNN Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=5)

    print("KNN model created.")
    print("K =", model.n_neighbors)


    # --------------------------------------------------
    # Step 7: Train Model
    # --------------------------------------------------

    print("\n" + border)
    print("Step 7: Train Model")
    print(border)

    model.fit(X_train_scaled, Y_train)

    print("Model training completed.")


    # --------------------------------------------------
    # Step 8: Make Predictions
    # --------------------------------------------------

    print("\n" + border)
    print("Step 8: Make Predictions")
    print(border)

    Y_pred = model.predict(X_test_scaled)

    print("Actual Values    :", Y_test.values)
    print("Predicted Values :", Y_pred)


    # --------------------------------------------------
    # Step 9: Calculate Accuracy
    # --------------------------------------------------

    print("\n" + border)
    print("Step 9: Model Evaluation")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Model Accuracy :", accuracy * 100, "%")


def main():
    data_path = "MarvellousInfosystems_PlayPredictor.csv"
    marvellous_classifier(data_path)

if __name__ == "__main__":
    main()
