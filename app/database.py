from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

engine = create_engine(os.getenv("DATABASE _ URL"))
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()