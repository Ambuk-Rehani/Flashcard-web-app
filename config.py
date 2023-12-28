import os
class Config:
    # FLASK_DEBUG = True
    # DEVELOPMENT = True
    SECRET_KEY = 'temporary'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgresql://myuser:mypassword@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
