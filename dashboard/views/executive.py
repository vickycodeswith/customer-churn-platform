import streamlit as st
import plotly.express as px

def show_executive_dashboard(df):
    st.header("📊 Executive Dashboard")

    total_customers = df.shape[0]
    churn_customers = df[df["Churn"] == "Yes"].shape[0]
    churn_rate = round((churn_customers / total_customers) * 100, 2)
    avg_monthly_charge = round(df["MonthlyCharges"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Total Customers", total_customers)
    col2.metric("🚨 Churned Customers", churn_customers)
    col3.metric("📉 Churn Rate", f"{churn_rate}%")
    col4.metric("💰 Avg Monthly Charge", f"${avg_monthly_charge}")

    st.subheader("Churn Distribution")

    churn_counts = df["Churn"].value_counts().reset_index()
    churn_counts.columns = ["Churn", "Count"]

    fig = px.pie(
        churn_counts,
        names="Churn",
        values="Count",
        title="Customer Churn Distribution"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("Contract Type vs Churn")

    fig2 = px.histogram(
        df,
        x="Contract",
        color="Churn",
        barmode="group",
        title="Contract Type vs Churn"
    )

    st.plotly_chart(fig2, width="stretch")