import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(path):
    return pd.csv(path)

def preprocess(df):
    df=df.copy()

    drop_col=["RowNumber","CustomerId","Surname"]
    for col in drop_col:
        if col in df.columns:
            df = df.drop(col,axis=1)
    
    le = LabelEncoder()
    for col in ['Geography','Gender']:
        df[col] = le.fit_transform(df[col])

    return df