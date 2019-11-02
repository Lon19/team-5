from flask import request, jsonify
from flask_restful import Resource
from .data_reader import all_data
import json

class GetWardData(Resource):
    def get(self):
        response = {
            'success': False,
            'errors': '',
            'data': '',
        }

        try:
            wardName = request.json.get('wardName')
            wardData = all_data[wardName]
            response = {
                'success': True,
                'errors': '',
                'data': {
                    wardName: wardData,
                },
            }
        except KeyError:
            response = {
                'success': False,
                'errors': 'Does not exists',
                'data': '',
            }
        except AttributeError:
            response = {
                'success': False,
                'errors': 'Wrong attributes',
                'data': '',
            }

        return jsonify(json.dumps(str(response)))
