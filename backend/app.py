import os
from flask import Flask, request, jsonify, make_response, render_template, Blueprint
from flask_restful import Api
from flask_cors import CORS
from resources.GetWardData import GetWardData
from resources.GetCoordinates import GetCoordinates
from resources.GetWards import GetWards
from resources.GetHighest import GetHighest
from resources.GetAllData import GetAllData
from resources.GetWardsUnemployment import GetWardsUnemployment


app = Flask(__name__, static_folder='../static/dist', template_folder='../static')
CORS(app)
app.config['SECRET_KEY'] =  os.urandom(24)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.register_blueprint(api_bp)

api.add_resource(GetWardData, '/GetWardData')
api.add_resource(GetCoordinates, '/GetCoordinates')
api.add_resource(GetWards, '/GetWards')
api.add_resource(GetWardsUnemployment, '/GetWardsUnemployment')
api.add_resource(GetHighest, '/GetHighest')
api.add_resource(GetAllData, '/GetAllData')



@app.errorhandler(404)
def handle_error(e):
    return make_response(jsonify({'error': '404: Not found'}), 404)

@app.errorhandler(500)
def handle_error(e):
    return make_response(jsonify({'error': '500: Internal server error'}), 500)

@app.errorhandler(403)
def handle_error(e):
    return make_response(jsonify({'error': '403: Unauthorized'}), 403)


if __name__ == '__main__':
    app.run()