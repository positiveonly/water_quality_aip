import streamlit as st
import pandas as pd
from model_utils import train_model, predict_sample

st.set_page_config(page_title="AI Water Quality Checker", layout="wide")
st.title("💧 AI-Powered Water Quality & Health Risk Checker")

menu = st.sidebar.radio("Choose Option", ["Train Model", "Single Entry", "Bulk CSV Upload"])

if menu == "Train Model":
    st.subheader("Train ML Model")
    clf = train_model()
    st.success("Model trained and saved as 'water_quality_model.pkl'.")

elif menu == "Single Entry":
    st.subheader("Enter Water Quality Parameters")
    sample = {
        "pH": st.number_input("pH", 0.0, 14.0, 7.0),
        "tds": st.number_input("TDS (mg/L)", 0, 2000, 300),
        "hardness": st.number_input("Hardness (mg/L)", 0, 1000, 150),
        "nitrate": st.number_input("Nitrate (mg/L)", 0, 200, 10),
        "chloride": st.number_input("Chloride (mg/L)", 0, 1000, 150),
        "fluoride": st.number_input("Fluoride (mg/L)", 0.0, 5.0, 1.0),
        "turbidity": st.number_input("Turbidity (NTU)", 0.0, 50.0, 2.0),
    }
    if st.button("Predict"):
        risk = predict_sample(sample)
        st.success(f"Predicted Water Risk Level: {risk}")

elif menu == "Bulk CSV Upload":
    st.subheader("Upload CSV File")
    file = st.file_uploader("Choose CSV", type=["csv"])
    if file:
        df = pd.read_csv(file)
        st.write("### Uploaded Data", df)
        predictions = []
        for _, row in df.iterrows():
            sample = {
                "pH": row["pH"],
                "tds": row["tds"],
                "hardness": row["hardness"],
                "nitrate": row["nitrate"],
                "chloride": row["chloride"],
                "fluoride": row["fluoride"],
                "turbidity": row["turbidity"],
            }
            predictions.append(predict_sample(sample))
        df["PredictedRisk"] = predictions
        st.write("### Predictions", df)
