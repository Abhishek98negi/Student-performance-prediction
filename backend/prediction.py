import os
import pandas as pd
import joblib

# 1. Get the absolute path to the directory where THIS python script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Join that directory with your filename
model_path = os.path.join(BASE_DIR, "model.joblib")

# 3. Load the model using the dynamic path
model = joblib.load(model_path)


def predict_marks( input_data: dict):
    df = pd.DataFrame([input_data])
    marks = model.predict(df)[0] 
    if marks < 0:
        marks = 0
    elif marks > 100:
        marks = 100   
    return float(marks)



# input  = {
#     "Attendance": 100,
#     "Test1": 40,
#     "Test2": 40,
#     "Assignment": 10,
#     "StudyHrs": 8
# }
# pred = predict_marks(input_data=input)
# print("Predicted Exam Marks:", round(pred, 2))


