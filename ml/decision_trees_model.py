import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle as pkl
from preprocessor import preprocess_data

def train_model(model_path="ml/models/decision_trees_model.pkl"):
    with open("ml/train_split.pkl", 'rb') as f:
        X_train, y_train = pkl.load(f)

    clf = DecisionTreeClassifier(max_depth=8, random_state=42, criterion='entropy', min_samples_split=5, min_samples_leaf=5)
    clf.fit(X_train, y_train)

    with open(model_path, 'wb') as f:
        pkl.dump(clf, f)
    
    print(f"Model trained and saved to {model_path}")


def evaluate_model(model_path="ml/models/decision_trees_model.pkl", test_split_path="ml/test_split.pkl"):
    with open(model_path, 'rb') as f:
        clf = pkl.load(f)
    
    with open(test_split_path, 'rb') as f:
        X_test, y_test = pkl.load(f)

    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=["No Disease", "Disease"])
    print("Decision Trees Model Evaluation:\n")
    print(report)

if __name__ == "__main__":
    # preprocess_data()
    # train_model()
    evaluate_model()
