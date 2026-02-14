import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY ="claveSecreta"
    SESSION_COOKIE_SECURE=False
    
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URL= 'mysql+pymysqk://root:admin@127.0.0.1/bdidgs805'
    SQLALCHEMY_TRACK_MODIFICATIONS=False