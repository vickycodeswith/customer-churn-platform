import streamlit as st

from predict_utils import prepare_input

def show_prediction_page(model, scaler, model_columns):
    st.header("🔮 Customer Churn Prediction")

    gender = st.selectbox("Gender", ["Male", "Female"], key="gender_input")
    senior_citizen = st.selectbox("Senior Citizen", [0, 1], key="senior_input")
    partner = st.selectbox("Partner", ["Yes", "No"], key="partner_input")
    dependents = st.selectbox("Dependents", ["Yes", "No"], key="dependents_input")
    tenure = st.slider("Tenure", 0, 72, 12, key="tenure_input")
    phone_service = st.selectbox("Phone Service", ["Yes", "No"], key="phone_input")
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"], key="multiple_lines_input")
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], key="internet_input")
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"], key="security_input")
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"], key="backup_input")
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"], key="device_input")
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"], key="tech_input")
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"], key="tv_input")
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"], key="movies_input")
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"], key="contract_input")
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"], key="billing_input")
    payment_method = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
        key="payment_input"
    )
    monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0, key="monthly_input")
    total_charges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0, key="total_input")

    if st.button("Predict Churn"):
        input_df = prepare_input(
            gender, senior_citizen, partner, dependents, tenure,
            phone_service, multiple_lines, internet_service, online_security,
            online_backup, device_protection, tech_support, streaming_tv,
            streaming_movies, contract, paperless_billing, payment_method,
            monthly_charges, total_charges, model_columns
        )

        numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
        input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error("Customer Likely To Churn")
        else:
            st.success("Customer Likely To Stay")

        st.metric("Churn Probability", f"{probability*100:.2f}%")

        if probability >= 0.80:
            st.warning("🔴 High Risk: Offer discount and retention support.")
        elif probability >= 0.50:
            st.info("🟡 Medium Risk: Send offers and engagement campaigns.")
        else:
            st.success("🟢 Low Risk: Continue regular engagement and loyalty rewards.")