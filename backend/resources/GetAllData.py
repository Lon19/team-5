from flask import request, jsonify
from flask_restful import Resource
from .data_reader import all_data
import json
import numpy


class GetAllData(Resource):
    def get(self):
        data = list(all_data.values())

        response = {
            'success': False,
            'errors': '',
            'data': data,
        }


        return jsonify(response)
