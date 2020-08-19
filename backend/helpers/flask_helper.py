# from flask_restful import reqparse
#
# parser = reqparse.RequestParser()
#
# def flask_parse_number(params):
#     args = parser.parse_args()

import json
from flask import jsonify, Response


def convert(data):
    if isinstance(data, bytes):  return json.loads(data.decode('ascii'))
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    return data

KEYS_TO_EXCLUDE = ['_sa_instance_state']

def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}

def parse_response(my_dict):
    if 'response' in my_dict and isinstance(my_dict['response'], dict):
        response_dict = without_keys(my_dict['response'], KEYS_TO_EXCLUDE)
        my_dict['response'] = response_dict

def flask_response(my_dict: dict):
    parse_response(my_dict)
    response = jsonify(my_dict)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def json_response(body='', **kwargs):
    body = json.dumps(body).encode('utf-8')
    status = kwargs['status'] or 200
    response = Response(body, status=status)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')
    return response












