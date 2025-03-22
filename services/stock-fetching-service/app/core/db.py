from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
import os
from app.core.config import config

DATABASE_URL = config.DATABASE_URL

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db_session = scoped_session(SessionLocal)
Base = declarative_base()

def get_db():
    """Dependency to get a database session"""
    db = db_session()
    try:
        yield db
    finally:
        db.close()
