#!/usr/bin/env python3

""" Auth module """

from flask import request, abort, jsonify

from api.v1.routes import api_route


@api_route.route('/auth', methods=['GET', 'POST'])
def auth():
    resp = {
        "message": "Authenticated",
        "user": "User"
    }
    return jsonify(resp)


@api_route.route('/auth/reset', methods=['POST'])
def reset_password():
    if request.method == "POST" and request.json:
        user = request.json.get('username')
        resp = {
            "message": "Password reset",
            "user": user
        }
        return jsonify(resp)

    return abort(405)
