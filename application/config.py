import os
from dotenv import load_dotenv
from pathlib import Path 

#set path to env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')