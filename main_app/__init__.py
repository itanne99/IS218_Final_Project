"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from ddtrace import patch_all

# Globally accessible libraries
db = SQLAlchemy()
r = FlaskRedis()
patch_all()

def create_app():
    """Construct the core flask_wtforms_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm"
    app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)

    with app.app_context():
        # Import parts of our flask_wtforms_tutorial
        from . import routes

        # Register Blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(admin.admin_bp)

        db.create_all()  # Create database tables for our data models

        return app
