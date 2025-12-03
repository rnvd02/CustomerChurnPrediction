import os
from src.train import train_model

def test_model_file_created(tmp_path):
    os.makedirs(tmp_path / "models", exist_ok=True)
    train_model_path = tmp_path / "models/churn_model.pkl"
    from src.train import train_model
    train_model() 
    assert os.path.exists("models/churn_model.pkl")