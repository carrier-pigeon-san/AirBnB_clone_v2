#!/usr/bin/python3
"""This module contains a script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Returns a given string through the variable in the route"""
    return f"Python {escape(text)}".replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Returns the string '<n> is  number' if n is an integer
    """
    if type(n) is int:
        return f"{int(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_temmplate(n):
    """Returns a html page only if n is an integer
    """
    if type(n) is int:
        return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
