import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(csv_path="sample_water_quality.csv"):
    df = pd.read_csv(csv_path)
    X = df.drop("OverallRisk", axis=1)
    y = df["OverallRisk"]
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    joblib.dump(clf, "water_quality_model.pkl")
    return clf

def predict_sample(sample_dict, model_path="water_quality_model.pkl"):
    import pandas as pd
    clf = joblib.load(model_path)
    X_new = pd.DataFrame([sample_dict])
    prediction = clf.predict(X_new)[0]
    return prediction
