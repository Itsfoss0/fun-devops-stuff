#!/usr/bin/env python3

""" Routes """

from flask import Blueprint

api_route = Blueprint("api", __name__,  url_prefix="/api/v1")

from api.v1.routes.products.products import *
from api.v1.routes.auth.auth import *