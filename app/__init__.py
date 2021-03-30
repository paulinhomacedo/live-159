from dynaconf import FlaskDynaconf, settings
from flask import Flask

from app.views import blueprints


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)

    print(settings.FLASK_ENV)

    register_blueprints(app)
    register_extensions(app)

    
    # @app.route('/')
    # def hello_world():
    #     return 'Hello, Mundaoo!'    
    return app     

def register_extensions(app):
    """Register Flask extensions."""
    pass


def register_blueprints(app):
    """Register application's blueprints"""
    for bp in blueprints:
        app.register_blueprint(bp)
