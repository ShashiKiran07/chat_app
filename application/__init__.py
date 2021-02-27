from flask import Flask
from application.config import Config
import os


# app = Flask(__name__)
# SECRET_KEY = os.getenv('SECRET_KEY1')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from application.routes import chat
    app.register_blueprint(chat)
    return app