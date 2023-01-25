import os

class Config():
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "appdata.db")

    SECRET_KEY = "0987987gw9s78gre8tg7s8876887ys8erg7y8s8eg7yserg78seyg87yh" ## move to os environ variable when you have data that matters; its a public repo

    SQLALCHEMY_TRACK_MODIFICATIONS = False

