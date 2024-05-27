#!/usr/bin/python3
"""Create view for State objects to handle all default RESTFul API actions"""

from flask import jsonify, abort, request
from models.city import City
from models.place import Place
from models import storage
from api.v1.views import app_views


@app_views.route('/cities/<string:city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places(city_id):
    """get place information for all places in a specified city"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    places = []
    for place in city.places:
        places.append(place.to_dict())
    return jsonify(places)


@app_views.route('/places/<string:place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """get place information for specified place"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<string:place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """deletes a place based on its place_id"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return (jsonify({}))


@app_views.route("/cities/<string:city_id>/places", methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """ function to create a place"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    city = storage.get("City", city_id)
    if not city:
        return abort(404)
    if not request.get_json():
        return abort(400, 'Not a JSON')
    kwarg = request.get_json()
    if 'name' not in kwarg:
        return abort(400, 'Missing name')
    place = Place(**kwarg)
    place.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<string:place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """function to update place """
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    place = storage.get("Place", place_id)
    if place:
        if not request.get_json():
            return abort(400, 'Not a JSON')
        date = request.get_json()
        ignore_keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

        for key, value in data.items():
            if key not in ignore_keys:
                setattr(place, key, value)
        place.save()
        return jsonify(place.to_dict()), 200
    else:
        return abort(404)
