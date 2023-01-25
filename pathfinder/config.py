import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='secrets.env')

class Config():
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "appdata.db")

    SECRET_KEY = os.environ.get('SECRET_KEY') ## move to os environ variable when you have data that matters; its a public repo

    SQLALCHEMY_TRACK_MODIFICATIONS = False

