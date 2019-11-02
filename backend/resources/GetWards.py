from flask import request, jsonify
from flask_restful import Resource
from .data_reader import all_data
import json


class GetWards(Resource):
    def get(self):
        wards = list(all_data.keys())
        response = {
            'success': True,
            'errors': '',
            'data': wards,
        }


        return jsonify(response)
