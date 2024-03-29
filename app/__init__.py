from flask import Flask
from flask_restful import Api

from app.main import routes as main_routes

def create_app(config_type : str):
    app = Flask(__name__)
    api = Api(app)

    # main/ routing
    api.add_resource(main_routes.Main, '/', '/<int:pk>')

    return app