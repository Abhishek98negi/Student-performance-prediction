from fastapi import FastAPI
from pydantic import BaseModel

from backend.prediction import predict_marks

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Student performance prediction",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change this to your frontend URL later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# input schema matching training features
class StudentPerformanceInput(BaseModel):
    Attendance: int
    Test1: int
    Test2: int
    Assignment: int
    StudyHrs: int
    

@app.get("/predict")
def predict_check():
    return {"status": "ok"}

# Student performance prediction endpoint
@app.post("/predict-student-performance")
def predict_student_performance(input_data: StudentPerformanceInput):
    input_data = input_data.model_dump()
    return predict_marks(input_data=input_data)


# uvicorn backend.main:app --reload
# http://127.0.0.1:8000/docs