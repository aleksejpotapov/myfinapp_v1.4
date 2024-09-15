from flask import Blueprint, render_template, request
from flask_cors import CORS, cross_origin
from flask import current_app as app
from flask.helpers import send_from_directory

core_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')

@app.route('/api', methods=['GET'])
@cross_origin()
def index():
    return {
        "tutorial": "Flask React Heroku"
    }

@app.route('/api', methods=['GET'])
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')