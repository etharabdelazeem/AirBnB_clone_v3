#!/usr/bin/python3
"""connects to the api"""
import os
from models import storage
from flask import Flask, Blueprint, make_response, jsonify

app = Flask(__name__)

from api.v1.views import app_views
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(code):
    """handels teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """a handler for 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')), threaded=True)
