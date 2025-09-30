import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    X = df.drop("charges", axis=1)
    y = df["charges"]
    categorical = ["sex", "smoker", "region"]
    numerical = ["age", "bmi", "children"]
    
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical),
            ("cat", OneHotEncoder(), categorical)
        ]
    )
    X_processed = preprocessor.fit_transform(X)
    return X_processed, y, preprocessor

def get_train_test(df, test_size=0.2, random_state=42):
    X = df.drop("charges", axis=1)
    y = df["charges"]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)