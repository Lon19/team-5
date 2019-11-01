from flask import request, jsonify
from flask_restful import Resource
from .data_reader import ward_data


class GetWardData(Resource):
    def get(self):
        response = {
            'success': False,
            'errors': '',
            'data': '',
        }
        try:
            wardName = request.json.get('wardName')
            wardData = ward_data[wardName]
            response = {
                'success': True,
                'errors': '',
                'data': {
                    wardName: wardData,
                },
            }
        except:
            response = {
                'success': False,
                'errors': '',
                'data': '',
            }

        return jsonify(response)
