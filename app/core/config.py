from datetime import timedelta
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())


JWT_SECRET_KEY = os.getenv('JWT_SECRET')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=45)
DATABASE_URL = os.getenv('DATABASE_URL')
