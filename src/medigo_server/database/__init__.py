from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("DB_URL")
SessionLocal = sessionmaker(bind=engine)