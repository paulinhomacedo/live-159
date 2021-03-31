from dynaconf import FlaskDynaconf
from flask import Flask

from app.ext import config


def create_app():
    app = Flask(__name__)
    config.init_app(app)
      
    return app     

