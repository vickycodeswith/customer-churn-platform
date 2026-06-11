import streamlit as st
import pandas as pd
import plotly.express as px

def show_model_insights():
    st.header("🧠 Model Insights")

    st.subheader("Model Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Model", "Random Forest")
    col2.metric("Problem Type", "Classification")
    col3.metric("Explainability", "SHAP")

    st.subheader("Top Churn Drivers")

    try:
        feature_df = pd.read_csv("data/processed/feature_importance.csv")

        fig = px.bar(
            feature_df.head(10),
            x="Importance",
            y="Feature",
            orientation="h",
            title="Top 10 Important Features"
        )

        st.plotly_chart(fig, width="stretch")

    except FileNotFoundError:
        st.warning("feature_importance.csv not found. Run model training notebook first.")

    st.info(
        """
        Key churn drivers usually include tenure, contract type, monthly charges,
        internet service, payment method, and support services.
        """
    )