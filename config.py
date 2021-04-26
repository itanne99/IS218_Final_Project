"""App configuration."""
import os
from os import environ


class Config:
    # General Config
    SECRET_KEY = os.urandom(32)
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
