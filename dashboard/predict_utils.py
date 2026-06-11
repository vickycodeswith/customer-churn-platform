import pandas as pd

def prepare_input(
    gender,
    senior_citizen,
    partner,
    dependents,
    tenure,
    phone_service,
    multiple_lines,
    internet_service,
    online_security,
    online_backup,
    device_protection,
    tech_support,
    streaming_tv,
    streaming_movies,
    contract,
    paperless_billing,
    payment_method,
    monthly_charges,
    total_charges,
    model_columns
):
    input_data = pd.DataFrame({
        "SeniorCitizen": [senior_citizen],
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],

        "gender_Male": [1 if gender == "Male" else 0],
        "Partner_Yes": [1 if partner == "Yes" else 0],
        "Dependents_Yes": [1 if dependents == "Yes" else 0],
        "PhoneService_Yes": [1 if phone_service == "Yes" else 0],
        "MultipleLines_No phone service": [1 if multiple_lines == "No phone service" else 0],
        "MultipleLines_Yes": [1 if multiple_lines == "Yes" else 0],

        "InternetService_Fiber optic": [1 if internet_service == "Fiber optic" else 0],
        "InternetService_No": [1 if internet_service == "No" else 0],

        "OnlineSecurity_No internet service": [1 if online_security == "No internet service" else 0],
        "OnlineSecurity_Yes": [1 if online_security == "Yes" else 0],

        "OnlineBackup_No internet service": [1 if online_backup == "No internet service" else 0],
        "OnlineBackup_Yes": [1 if online_backup == "Yes" else 0],

        "DeviceProtection_No internet service": [1 if device_protection == "No internet service" else 0],
        "DeviceProtection_Yes": [1 if device_protection == "Yes" else 0],

        "TechSupport_No internet service": [1 if tech_support == "No internet service" else 0],
        "TechSupport_Yes": [1 if tech_support == "Yes" else 0],

        "StreamingTV_No internet service": [1 if streaming_tv == "No internet service" else 0],
        "StreamingTV_Yes": [1 if streaming_tv == "Yes" else 0],

        "StreamingMovies_No internet service": [1 if streaming_movies == "No internet service" else 0],
        "StreamingMovies_Yes": [1 if streaming_movies == "Yes" else 0],

        "Contract_One year": [1 if contract == "One year" else 0],
        "Contract_Two year": [1 if contract == "Two year" else 0],

        "PaperlessBilling_Yes": [1 if paperless_billing == "Yes" else 0],

        "PaymentMethod_Credit card (automatic)": [1 if payment_method == "Credit card (automatic)" else 0],
        "PaymentMethod_Electronic check": [1 if payment_method == "Electronic check" else 0],
        "PaymentMethod_Mailed check": [1 if payment_method == "Mailed check" else 0],
    })

    input_data = input_data.reindex(
        columns=model_columns,
        fill_value=0
    )

    return input_data