#!/usr/bin/python3
"""a module that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnd():
    """return the string “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return the string “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """return C followed with a text"""
    text = text.replace('_', " ")
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_func(text='is cool'):
    """return the string 'python' with some text"""
    text = text.replace('_', " ")
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """return n if it's a number"""
    return f'{str(n)} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """render a template with the variable
    passed as argument"""
    return render_template('5-number.html', n=n)


@app.route('/airbnb-dynamic/number_odd_or_even/<int:n>', strict_slashes=False)
app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
