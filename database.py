from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
데이터베이스와 관련된 설정
'''

SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi_pj.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}# check_same_thread : 멀티 스레드 허용
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # ORM을 상속할 기본 class 

# 
def get_db():
    db = SessionLocal()
    try:
        yield db # 함수의 실행을 중지하고 객체 반환.
    finally:
        db.close() # try블록이 끝나거나, 예외 발생되도 실행
