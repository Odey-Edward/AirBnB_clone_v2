#!/usr/bin/python3
"""A flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """serve web page upon request to /states_list URL"""
    all_state = storage.all(State)
    return render_template('7-states_list.html', states=all_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500)
