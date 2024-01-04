#!/usr/bin/python3
"""A flask web application listening
on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """return all States"""
    states = storage.all(State)
    if not id:
        return render_template('9-states.html', states=states, id=id)

    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state)

    return render_template('9-states.html')


@app.teardown_appcontext
def cleanup(exc):
    """clear and close the database
    connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
