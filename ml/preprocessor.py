import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle as pkl

def preprocess_data(data_path="data/processed.cleveland.data"):
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

    with open("ml/train_split.pkl", 'wb') as f:
        pkl.dump((X_train, y_train), f)

    with open("ml/test_split.pkl", 'wb') as f:
        pkl.dump((X_test, y_test), f)

if __name__ == "__main__":
    preprocess_data()