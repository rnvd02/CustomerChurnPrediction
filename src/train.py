import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from preprocess import load_data,preprocess

def train_model():
    df= load_data("data/Churn_Modelling.csv")
    df=preprocess(df)

    X=df.drop("Exited",axis=1)
    y=df["Exited"]

    X_train,y_train,X_test,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    model=RandomForestClassifier(n_estimators=150,random_state=42)
    model.fit(X_train,y_train)

    joblib.dump(model,"models/churn_model.pkl")
    print("Model saved to models/churn_model.pkl")

if __name__=="main":
    train_model()