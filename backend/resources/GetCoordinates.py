from flask import request, jsonify
from flask_restful import Resource
from .data_reader import all_data
import requests

class FAILED_TO_FETCH_WARD_FROM_POSTCODE(Exception):
    pass

class GetCoordinates(Resource):
    def get(self):
        response = {}

        try:
            post_code = request.json.get('postCode')
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
                'errors': e,
                'data': '',
            }
        return jsonify(response)

    def postCodeToWard(postcode):
        res = requests.get('https://api.postcodes.io/postcodes/'+postcode)
        if res.ok:
            ward_name = res.json()['result']['admin_ward']
            return all_data[ward_name]
        else:
            raise FAILED_TO_FETCH_WARD_FROM_POSTCODE("ERROR "+str(res.status_code) + " " + res.json()['error'])
            