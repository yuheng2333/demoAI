from flask import make_response, jsonify


def response_obj(data, status):
    response = make_response(jsonify(data))
    response.status_code = status
    return response