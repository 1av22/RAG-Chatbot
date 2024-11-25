from src.models.userModel import User, File

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base for models
Base = declarative_base()
load_dotenv()

# Define your database URL here
POSTGRE_USER = os.getenv("POSTGRE_USER")
POSTGRE_PASSWORD = os.getenv("POSTGRE_PASSWORD")
POSTGRE_HOST = os.getenv("POSTGRE_HOST")
DB_NAME = "ragChatbot"
DATABASE_URL = f"postgresql://{POSTGRE_USER}:{
    POSTGRE_PASSWORD}@{POSTGRE_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
