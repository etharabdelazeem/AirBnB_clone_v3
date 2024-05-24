#!/usr/bin/python3
"""app views index"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """returns JSON status"""
    return jsonify({"status": "OK"})
