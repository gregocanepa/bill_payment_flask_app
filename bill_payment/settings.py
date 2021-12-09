import os

file_path = os.path.abspath(os.getcwd())+"/bill_payment.db"

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+file_path
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
