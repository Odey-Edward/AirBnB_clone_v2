#!/usr/bin/python3
from flask import Flask
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    #all_state = storage.all(State)
    return 'Hello Edward'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
