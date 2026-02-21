import time
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://user:password@db:5432/tasks"

# Czekanie na bazę
while True:
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        print("✅ Połączono z bazą danych!")
        break
    except OperationalError:
        print("⏳ Czekam na bazę danych...")
        time.sleep(2)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

app = FastAPI()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Task Manager API działa 🚀"}

@app.post("/tasks/")
def create_task(title: str):
    db = SessionLocal()
    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task