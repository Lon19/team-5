from flask import request, jsonify
from flask_restful import Resource
from .data_reader import all_data
import json
import numpy



def getHighests(limit=5):
    highest = [0 for _ in range(limit)]
    highest_names = ['' for _ in range(limit)]
    for ward in all_data.keys():
        if all_data[ward]['Total'] > highest[0]:
            highest[0] = all_data[ward]['Total']
            highest_names[0] = ward
            highest_names = [x for _,x in sorted(zip(highest, highest_names))]
            highest = sorted(highest)

    results = [all_data[name] for name in highest_names if name != '']
    return results


class GetHighest(Resource):
    def get(self):
        response = {
            'success': False,
            'errors': '',
            'data': '',
        }

        try:
            limit = int(request.headers.get('limit'))
            data = getHighests(limit)
            response = {
                'success': True,
                'errors': '',
                'data': data,
            }
        except AttributeError:
            response = {
                'success': False,
                'errors': 'Wrong attributes',
                'data': '',
            }

        return jsonify(response)
