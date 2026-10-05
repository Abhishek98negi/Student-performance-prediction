import os
import requests
import streamlit as st


# API_URL = "http://127.0.0.1:8000/predict-student-performance"

# Defaults to localhost for local testing, uses Render URL in production
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="👨‍🎓",
    layout="centered"
)

st.title("Predict student's performance in upcomming exam")

st.subheader("Enter Student's details and click **Predict**")

col1, col2 = st.columns(2)

with col1:
    attendance = st.number_input(
        "Attendance percentage",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        placeholder="Enter attendance percentage"
    )
    test1 = st.number_input(
        "Test 1 Score out of 40",
        min_value=0.0,
        max_value=40.0,
        value=0.0,
        placeholder="Enter Test 1 score"
    )
    test2 = st.number_input(
        "Test 2 Score out of 40",
        min_value=0.0,
        max_value=40.0,
        value=0.0,
        placeholder="Enter Test 2 score"
    )
    
with col2:
    assignment = st.number_input(
        "Assignment Score out of 10",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        placeholder="Enter Assignment score"
    )
    study_hours = st.number_input(
        "Study Hours per day",
        min_value=0.0,
        max_value=20.0,
        value=0.0,
        placeholder="Enter study hours"
    )


if st.button("🔍 Predict"):
    if attendance is None or test1 is None or test2 is None or assignment is None or study_hours is None:
        st.error("Please fill in all the fields.")
    else:
        input_data = {
            "Attendance": attendance,
            "Test1": test1,
            "Test2": test2,
            "Assignment": assignment,
            "StudyHrs": study_hours
        }

        response = requests.post(f"{BACKEND_URL}/predict-student-performance", json=input_data)
        # response = requests.post(API_URL, json=input_data)

        if response.status_code != 200:
            st.error("Something went wrong. Try again later...")
        else:
            result = response.json() 

            st.divider()

            st.metric(
                label="Predicted Exam Marks out of 100",
                value=f'{result:.2f}%'
            )

           

# streamlit run frontend/app.py