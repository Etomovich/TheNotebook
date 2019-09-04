'''makes note_app a module'''
import os
from flask import Flask
from instance.config import config_classes


def create_app():
    '''This method creates the flask instance and returns it.'''
    app = Flask(__name__)
    flask_environment = os.environ.get("BASE_ENVIRONMENT")
    app.config.from_object(config_classes[flask_environment])

    return app
