from flask import request, jsonify
from flask_restful import Resource
from .data_reader import all_data, postCodeToWard, FAILED_TO_FETCH_WARD_FROM_POSTCODE


class GetCoordinates(Resource):
    def get(self):
        response = {}

        try:
            post_code = request.headers.get('postCode')
            _data = postCodeToWard(post_code)
            
            response = {
                'success': True,
                'errors': '',
                'data': {
                    'ward_data': _data
                }
            }
        except FAILED_TO_FETCH_WARD_FROM_POSTCODE as e:
            response = {
                'success': False,
                'errors': str(e),
                'data': '',
            }
        return jsonify(response)
            