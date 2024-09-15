from flask import Flask
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory

cors = CORS() 

def create_app():

    # Initialize the core application
    app = Flask(__name__, static_folder="../myfinapp-react-v1.4/build", static_url_path="")
    app.config.from_object('server.config.DevelopmentConfig')

    # initialize plugins
    cors.init_app(app)

    #change

    with app.app_context():

        #import routes and models
        from .a_core import core

        #Register blueprints
        app.register_blueprint(core.core_bp) 

    return app
