import os

file_path = os.path.abspath(os.getcwd())+"/bill_payment.db"


class Config:
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+file_path
