from flask import Flask
from server.blueprints import core_routes


def create_app():
    app = Flask(__name__)

    app.register_blueprint(core_routes)

    return app
