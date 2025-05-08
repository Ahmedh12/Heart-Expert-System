# ml/model_trainer.py

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle as pkl

def train_model(data_path="data/processed.cleveland.data", model_path="ml/heart_model.pkl"):
    columns = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
    ]

    df = pd.read_csv(data_path, header=None, names=columns)

    df.replace('?', np.nan, inplace=True)
    df = df.apply(pd.to_numeric, errors='coerce')
    df.dropna(inplace=True)

    df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

    X = df.drop(columns=['target'])
    y = df['target']

    X_train, X_test , y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = DecisionTreeClassifier(max_depth=5, random_state=42)
    clf.fit(X_train, y_train)

    with open(model_path, 'wb') as f:
        pkl.dump(clf, f)
    
    with open("ml/test_split.pkl", 'wb') as f:
        pkl.dump((X_test, y_test), f)

    print(f"Model trained and saved to {model_path}")


def evaluate_model(model_path="ml/heart_model.pkl", test_split_path="ml/test_split.pkl"):
    with open(model_path, 'rb') as f:
        clf = pkl.load(f)
    
    with open(test_split_path, 'rb') as f:
        X_test, y_test = pkl.load(f)

    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=["No Disease", "Disease"])
    print("Model Evaluation:\n")
    print(report)

if __name__ == "__main__":
    train_model()
    evaluate_model()
