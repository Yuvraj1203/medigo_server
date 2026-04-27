from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from typing import Generator

SQLALCHEMY_DATABASE_URL = "DB_URL"

engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Dependency
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()