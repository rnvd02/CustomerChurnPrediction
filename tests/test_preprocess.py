from src.preprocess import preprocess
import pandas as pd

def test_preprocess():
    df=pd.DataFrame({
        "RowNumber": [1],
        "CustomerId": [12345],
        "Surname": ["Smith"],
        "CreditScore": [600],
        "Geography": ["France"],
        "Gender": ["Male"],
        "Age": [40],
        "Balance": [100.0],
        "EstimatedSalary": [50000],
        "Exited": [1]
    })
    
    out = preprocess(df)
    assert "RowNumber" not in out.columns
    assert "CustomerId" not in out.columns
    assert "Surname" not in out.columns