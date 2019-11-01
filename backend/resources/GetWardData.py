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


        dummy_data = {
            'success': False,
            'errors': '',
            'data': {
                'wardName': 'Middleton St George',
                'long': '-1.47437',
                'lat': '54.55521011',
            },
        }

        return jsonify(dummy_data)
