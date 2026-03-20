from fastapi import FastAPI
# from app.core.config import settings
# print(f"Database URL: {settings.DATABASE_URL}")
from sqlalchemy import text



app = FastAPI(
    title="Expense Tracker API",
      description="API for tracking expenses",
        version="1.0.0")
@app.get("/")
def health_check():
    return{"status": "API is up and running!"}

from app.db.database import Base, engine
from app.models import expense
from app.models import user

Base.metadata.create_all(bind=engine)