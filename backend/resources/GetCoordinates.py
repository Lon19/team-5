from flask import request, jsonify
from flask_restful import Resource
from .data_reader import all_data
import requests
import numpy
import collections
import math



class FAILED_TO_FETCH_WARD_FROM_POSTCODE(Exception):
    pass


def euclidean_dist(x, y):
    """
    Parameters
    ----------
    a: list (x, y)
    b: list (x, y)
    """
    # return math.sqrt(numpy.linalg.norm(a[0] - b[0]) + numpy.linalg.norm(a[1] - b[1]))
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))


def postCodeToWard(postcode, nearests=3):
    res = requests.get('https://api.postcodes.io/postcodes/'+postcode)
    if res.ok:
        ward_name = res.json()['result']['admin_ward'].lower()
    else:
        raise FAILED_TO_FETCH_WARD_FROM_POSTCODE(
            "ERROR "+str(res.status_code) + " " + res.json()['error'])

    ward_point = [float(all_data[ward_name]['lat']), float(all_data[ward_name]['long'])]
    nearests_dist = [100000000 for _ in range(nearests)]
    nearests_names = ['' for _ in range(nearests)]
    for ward in all_data.keys():
        candidate_point = [float(all_data[ward]['lat']), float(all_data[ward]['long'])]
        candidate_dist = euclidean_dist(candidate_point, ward_point)

        if candidate_dist < nearests_dist[-1]:
            nearests_dist[-1] = candidate_dist
            nearests_names[-1] = ward
            nearests_names = [x for _,x in sorted(zip(nearests_dist, nearests_names))]
            print(nearests_names)
            nearests_dist = sorted(nearests_dist)
            print(nearests_dist)

    results = [all_data[name] for name in nearests_names]
    return results


class GetCoordinates(Resource):
    def get(self):
        response = {}

        try:
            post_code = request.headers.get('postCode')
            nearests = request.headers.get('nearests')
            data = postCodeToWard(post_code, int(nearests))

            response = {
                'success': True,
                'errors': '',
                'data': data,
            }
        except FAILED_TO_FETCH_WARD_FROM_POSTCODE as e:
            response = {
                'success': False,
                'errors': str(e),
                'data': '',
            }

        return jsonify(response)
