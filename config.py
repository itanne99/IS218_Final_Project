"""App configuration."""
import os
from os import environ


class Config:
    # General Config
    SECRET_KEY = os.urandom(32)
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://xuvwzq6wygw6t2gv:znabbsq170mffx5r@pxukqohrckdfo4ty.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/hprxc6b8d6lbq5gf"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
