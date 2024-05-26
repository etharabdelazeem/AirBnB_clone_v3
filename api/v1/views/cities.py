#!/usr/bin/python3
"""Create view for State objects to handle all default RESTFul API actions"""

from flask import jsonify, abort, request
from models.state import State
from models.city import City
from models import storage
from api.v1.views import app_views


@app_views.route ('/states/<state_id>/cities', strict_slashes=False)
def getAllcities(state_id):
    """function to get all city object of a state """
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(city_id)
 
@app_views.route ('/cities/<city_id>', strict_slashes=False)
def get_city(state_id):
    """function to get a city"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(state.to_dict())
    else:
        return abort(404)


@app_views.route('/cities/<cities_id>', methods= ['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """ function to delete a city"""
    state = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """ function to create city"""
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    if not request.get_json():
        return abort(400, 'Not a JSON')
    kwarg = request.get_json()
    if 'name' not in kwarg:
        return abort(400, 'Missing name')
    city = City(**kwarg)
    city.save()
    return jsonify(city.to_dict()), 201


 
@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """function to update city """
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    city = storage.get(City, city_id)
    if city:
        if not request.get_json():
            return abort(400, 'Not a JSON')
        date = request.get_json()
        ignore_keys = ['id', 'created_at', 'updated_at']

        for key, value in data.items():
            if key not in ignore_keys:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
    else:
        return abort(404)
