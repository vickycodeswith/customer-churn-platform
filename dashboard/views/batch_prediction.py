import streamlit as st
import pandas as pd

def show_batch_prediction(model, scaler, model_columns):

    st.header("📁 Batch CSV Churn Prediction")

    uploaded_file = st.file_uploader(
        "Upload customer CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Data Preview")
        st.dataframe(df.head())

        required_columns = [
            "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
            "PhoneService", "MultipleLines", "InternetService",
            "OnlineSecurity", "OnlineBackup", "DeviceProtection",
            "TechSupport", "StreamingTV", "StreamingMovies",
            "Contract", "PaperlessBilling", "PaymentMethod",
            "MonthlyCharges", "TotalCharges"
        ]

        missing_cols = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing_cols:
            st.error(f"Missing columns: {missing_cols}")
            return

        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

        df["TotalCharges"] = df["TotalCharges"].fillna(
            df["TotalCharges"].median()
        )

        input_df = df[required_columns].copy()

        input_encoded = pd.get_dummies(
            input_df,
            drop_first=True
        )

        input_encoded = input_encoded.reindex(
            columns=model_columns,
            fill_value=0
        )

        numeric_cols = [
            "tenure",
            "MonthlyCharges",
            "TotalCharges"
        ]

        input_encoded[numeric_cols] = scaler.transform(
            input_encoded[numeric_cols]
        )

        predictions = model.predict(input_encoded)
        probabilities = model.predict_proba(input_encoded)[:, 1]

        df["Churn_Prediction"] = [
            "Yes" if pred == 1 else "No"
            for pred in predictions
        ]

        df["Churn_Probability"] = probabilities

        df["Risk_Level"] = df["Churn_Probability"].apply(
            lambda x: "High Risk" if x >= 0.80
            else "Medium Risk" if x >= 0.50
            else "Low Risk"
        )

        st.subheader("Prediction Results")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Prediction CSV",
            csv,
            "churn_predictions.csv",
            "text/csv"
        )