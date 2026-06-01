import streamlit as st

st.set_page_config(page_title="Bank Customer Churn Prediction")

st.title("🏦 Bank Customer Churn Prediction")

st.write("Customer Churn Risk Calculator")

credit_score = st.number_input("Credit Score", 300, 900, 650)
age = st.number_input("Age", 18, 100, 35)
balance = st.number_input("Balance", 0.0, 500000.0, 50000.0)
products = st.number_input("Number of Products", 1, 4, 2)
active = st.selectbox("Active Member", ["Yes", "No"])

if st.button("Predict Risk"):

    risk = 0

    if age > 45:
        risk += 30

    if products == 1:
        risk += 25

    if active == "No":
        risk += 35

    if balance > 100000:
        risk += 10

    st.subheader(f"Risk Score: {risk}%")

    if risk >= 60:
        st.error("High Churn Risk")
    elif risk >= 30:
        st.warning("Medium Churn Risk")
    else:
        st.success("Low Churn Risk")
