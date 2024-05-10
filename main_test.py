from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.gzip import GZipMiddleware
import datetime as dt
import logging


# uvicorn main:app --reload
# FastAPI 애플리케이션 생성
app = FastAPI() 
logger = logging.getLogger(__name__)

app.add_middleware(GZipMiddleware)

class UnicornException(Exception):
    def __init__(self, value: str):
        self.value = value

class Student(BaseModel):
    name: str
    roll_number: int

students = {
    1: Student(name="GK", roll_number=4),
    2: Student(name="ST", roll_number=5),
    3: Student(name="MF", roll_number=6),
}
'''
# 루트 웹 주소에서 경로 정의 ("/") 
@app.get( "/" ) 
def  read_root (): 
    return { "message" : "Hello , FastAPI!" }
'''
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Student with particular roll number does noet exist."},
    )

@app.get("/items/{roll_number}")
def query_student_by_roll_number(roll_number: int):
    if roll_number not in students:
        raise UnicornException(value=roll_number)
    return students[roll_number]
    
# Handle the startup event
@app.on_event("startup")
async def custom_startup_function():
    print('FastAPI Server started :', dt.datetime.now())

@app.on_event("shutdown")
async def event_shutdown():
    print('FastAPI Server shutdown :', dt.datetime.now())