#!/usr/bin/env python3


from flask import request, abort, jsonify

from api.v1.routes import api_route


@api_route.route('/', methods=['GET'])
def all_products():
    """ Return all products in the store """
    products = {
        "food": {
            "price": "22",
        },
        "clothing": {
            "price": 99
        },
        "guns": {
            "price": 33
        }
    }
    return jsonify(
        {
            "message": "Products in stock",
            "data": products
        }
    )


@api_route.route('/foo', methods=['GET'])
def foo():
    return jsonify({
        "message": "Foo",
        "products": ["foo", "bar"]
    })

@api_route.route('/bar', methods=['GET'])
def bar():
    return jsonify({
        "message": "Bar",
        "products": ["foo", "bar"]
    })
    
@api_route.route('/status', methods=['GET', 'POST'])
def status():
    return jsonify({
        "status": "ok"
    })