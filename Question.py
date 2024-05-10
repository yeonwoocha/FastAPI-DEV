from models import Question, Answer
from datetime import datetime
from database import SessionLocal


db = SessionLocal()

q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())

db.add(q)
db.commit()