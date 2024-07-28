#!/usr/bin/python3
"""This module contains a script that starts a Flask web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Returns a given string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Returns a given string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Returns a given string through the variable in the route"""
    return f"C {escape(text)}".replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
