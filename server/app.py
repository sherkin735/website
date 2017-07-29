from flask import Flask
from server.blueprints import core_routes


def create_app():
    app = Flask(__name__, static_folder='foo/cache/')

    app.register_blueprint(core_routes)

    return app