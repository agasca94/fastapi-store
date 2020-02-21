from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

SQL_ALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
