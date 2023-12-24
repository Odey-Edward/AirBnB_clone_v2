#!/usr/bin/python3
"""a module that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnd():
    """return the string “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """return the string “HBNB”"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
