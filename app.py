import streamlit as st
import pickle

st.title("Salary Predictor")
st.set_page_config(page_title="Salary Predictor",page_icon="💵")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

exp = st.number_input("Enter Years of Experience", min_value=0.0, max_value=11.0, value=1.0, step=0.5)

if st.button("Predict Salary"):
    predicted_salary = model.predict([[exp]])[0]
    st.success(predicted_salary)

