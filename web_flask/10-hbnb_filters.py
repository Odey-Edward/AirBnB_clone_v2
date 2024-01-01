#!/usr/bin/python3
"""A flask web application listening
on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """return a html template containing
    the state, cities and amenities"""
    states = storage.all(State)
    amenity = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', states=states, amenities=amenity)


@app.teardown_appcontext
def cleanup(exc):
    """clear and close the database
    connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
