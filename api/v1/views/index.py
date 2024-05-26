#!/usr/bin/python3
"""app views index"""
from api.v1.views import app_views
from flask import jsonify

classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route("/status")
def status():
    """returns JSON status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    """retrieves the number of each objects by type"""
    dictionary = {}
    for key, value in classes.items():
        dictionary[key] = storage.count(value)
    return jsonify(dictionary)
