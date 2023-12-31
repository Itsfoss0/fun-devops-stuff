#!/usr/bin/env python3


""" Main application """

from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.routes import api_route


app = Flask(__name__)
app.register_blueprint(api_route)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)