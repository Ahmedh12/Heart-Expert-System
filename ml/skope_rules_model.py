import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from skrules import SkopeRules
import pickle as pkl
from preprocessor import preprocess_data

def train_model(model_path="ml/models/skope_rules_model.pkl"):
    with open("ml/train_split.pkl", 'rb') as f:
        X_train, y_train = pkl.load(f)

    clf = SkopeRules(
        feature_names=X_train.columns.tolist(),
        precision_min=0.6,
        recall_min=0.4,
        n_estimators=50,
        max_depth=8
    )
    clf.fit(X_train.values, y_train.values)

    with open(model_path, 'wb') as f:
        pkl.dump((clf, X_train.columns.tolist()), f)

    print(f"Model trained and saved to {model_path}")

def train_model_with_inverted_target(model_path="ml/models/skope_rules_model_inverted_target.pkl"):
    with open("ml/train_split.pkl", 'rb') as f:
        X_train, y_train = pkl.load(f)

    y_train_inverted = 1 - y_train  # Now class 0 becomes class 1 and class 1 becomes class 0

    clf = SkopeRules(
        feature_names=X_train.columns.tolist(),
        precision_min=0.6,
        recall_min=0.4,
        n_estimators=50,
        max_depth=8
    )
    clf.fit(X_train.values, y_train_inverted.values)

    with open(model_path, 'wb') as f:
        pkl.dump((clf, X_train.columns.tolist()), f)

    print(f"Model trained with inverted target and saved to {model_path}")

def evaluate_model(model_path="ml/models/skope_rules_model.pkl", test_split_path="ml/test_split.pkl"):
    with open(model_path, 'rb') as f:
        clf, feature_names = pkl.load(f)
    
    with open(test_split_path, 'rb') as f:
        X_test, y_test = pkl.load(f)

    y_pred = clf.predict(X_test.values)
    report = classification_report(y_test, y_pred, target_names=["No Disease", "Disease"])
    print("SkopeRules Model Evaluation:\n")
    print(report)

    num_rules = len(clf.rules_)
    print(f"Number of rules: {num_rules}\n")

def evaluate_model_with_inverted_target(model_path="ml/models/skope_rules_model_inverted_target.pkl", test_split_path="ml/test_split.pkl"):
    with open(model_path, 'rb') as f:
        clf, feature_names = pkl.load(f)
    
    with open(test_split_path, 'rb') as f:
        X_test, y_test = pkl.load(f)

    y_pred = clf.predict(X_test.values)

    y_pred_original = 1 - y_pred

    report = classification_report(y_test, y_pred_original, target_names=["No Disease", "Disease"])
    print("Inverted SkopeRules Model Evaluation:\n")
    print(report)

    num_rules = len(clf.rules_)
    print(f"Number of rules: {num_rules}\n")


if __name__ == "__main__":
    # preprocess_data()
    # train_model()
    evaluate_model()
    # train_model_with_inverted_target()
    evaluate_model_with_inverted_target()