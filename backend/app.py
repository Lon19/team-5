from flask import Flask, request, jsonify, make_response, render_template, Blueprint
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__, static_folder='../static/dist', template_folder='../static')
CORS(app)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.register_blueprint(api_bp)




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