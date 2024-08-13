import mlflow
import mlflow.sklearn
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier()
# Start an MLflow run
with mlflow.start_run(run_name=f"GitCopyCap"):
    mlflow.autolog()
    # Train the classifier
    clf.fit(X_train, y_train)
    # Predict the test set
    y_pred = clf.predict(X_test)
    # Calculate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    # Log the accuracy to MLflow
    mlflow.log_metric("accuracy", accuracy)
    # Log the model
    mlflow.sklearn.log_model(clf, "decision_tree_model")
    # Log the model parameters
    mlflow.log_params(clf.get_params())
    # Print the accuracy
    print(f'Accuracy: {accuracy:.2f}')
    # Output some predictions and their corresponding actual labels
    print("\nSample predictions:")
    for i in range(5):
        print(f'Predicted: {y_pred[i]}, Actual: {y_test[i]}')