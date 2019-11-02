from flask import request, jsonify
from flask_restful import Resource
from .data_reader import all_data
import json


class GetWardsUnemployment(Resource):
    def get(self):
        response = {
            'success': False,
            'errors': '',
            'data': '',
        }

        try:
            unemployment_number = request.headers.get('unemployment_number')
            gender = request.headers.get('gender') # Total, Male, Female
            wards = []
            for ward in all_data.keys():
                if int(all_data[ward][gender]) > int(unemployment_number):
                    wards.append(all_data[ward])

            response = {
                'success': True,
                'errors': '',
                'data': wards,
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

        return jsonify(response)
