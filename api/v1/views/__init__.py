#!/usr/bin/python3
"""init file"""
from api.v1.views.index import *
from flask import Blueprint
from flask import Flask

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
