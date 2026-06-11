import streamlit as st

def show_business_recommendations():
    st.header("💡 Business Recommendations")

    st.markdown("""
    ### 🔴 High Risk Customers
    - Offer immediate discount or retention package
    - Assign customer success representative
    - Investigate service quality issues
    - Promote annual or two-year contract

    ### 🟡 Medium Risk Customers
    - Send personalized email campaigns
    - Offer loyalty benefits
    - Recommend better plans
    - Monitor engagement regularly

    ### 🟢 Low Risk Customers
    - Continue regular engagement
    - Maintain service quality
    - Offer occasional loyalty rewards
    - Encourage referrals
    """)

    st.success("These actions help reduce churn and improve customer retention.")