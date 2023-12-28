#!/usr/bin/python3
"""A flask web application listening
on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """return all cities with thier
    corresponding state"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def cleanup(exc):
    """clear and close the database
    connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
