from flask import Flask
from server.blueprints.core_routes import core_routes


def create_app():
    app = Flask(__name__)

    app.register_blueprint(core_routes)

    return app
