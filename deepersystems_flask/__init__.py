from flask import Flask
from .extentions import mongo
from .config import Config
from .views import routes


def create_app():
    """Create app function to handle instantiation of Flask app and to be able to use outside of context if needed"""

    app = Flask(__name__)

    app.config.from_object(Config)

    mongo.init_app(app)

    # register blueprints to app
    app.register_blueprint(routes.main)

    return app

