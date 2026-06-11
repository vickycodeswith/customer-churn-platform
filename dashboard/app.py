import streamlit as st
import pandas as pd
import pickle

from views.executive import show_executive_dashboard
from views.prediction import show_prediction_page
from views.model_insights import show_model_insights
from views.business_recommendations import show_business_recommendations
from views.batch_prediction import show_batch_prediction

st.set_page_config(
    page_title="Customer Churn Prediction Platform",
    page_icon="📊",
    layout="wide"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/Telco-Customer-Churn.csv")
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())
    return df

@st.cache_resource
def load_model_files():
    with open("models/random_forest.pkl", "rb") as file:
        model = pickle.load(file)

    with open("models/scaler.pkl", "rb") as file:
        scaler = pickle.load(file)

    with open("models/model_columns.pkl", "rb") as file:
        model_columns = pickle.load(file)

    return model, scaler, model_columns

df = load_data()
model, scaler, model_columns = load_model_files()

st.markdown("""
<h1 style='text-align:center;'>📊 Customer Churn Prediction Platform</h1>
<p style='text-align:center; color:#94a3b8; font-size:18px;'>
AI-powered churn prediction, explainability and retention recommendation dashboard
</p>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="brand-box">
    <div class="brand-title">ChurnAI</div>
    <p>Customer Retention Intelligence</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.selectbox(
    "Navigation",
    [  
        "📁 Batch CSV Prediction",
        "📊 Executive Dashboard",
        "🔮 Customer Prediction",
        "🧠 Model Insights",
        "💡 Business Recommendations"
        
    ]
)

if page == "📊 Executive Dashboard":
    show_executive_dashboard(df)

elif page == "🔮 Customer Prediction":
    show_prediction_page(model, scaler, model_columns)

elif page == "🧠 Model Insights":
    show_model_insights()

elif page == "💡 Business Recommendations":
    show_business_recommendations()

elif page == "📁 Batch CSV Prediction":
    show_batch_prediction(model, scaler, model_columns)


