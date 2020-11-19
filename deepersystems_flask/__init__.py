from flask import Flask
from .extentions import mongo, bootstrap
from .config import Config
from .views.main_routes import main
from .views.theme_routes import theme


def create_app():
    """Create app function to handle instantiation of Flask app and to be able to use outside of context if needed"""

    app = Flask(__name__)

    app.config.from_object(Config)

    mongo.init_app(app)

    bootstrap.init_app(app)

    # register blueprints to app
    app.register_blueprint(main)
    app.register_blueprint(theme)

    return app

