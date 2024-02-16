#!/usr/bin/python3
"""
a flsk script that starts a flask web application listening on
0.0.0.0 port 5000
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """first flask funtion"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """a new route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def dynamic_text(text):
    """dynamicaly printint text"""
    return "C {:s}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<string:text>", strict_slashes=False)
def python_text(text):
    """defalut text and dynamic text in thesame route"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def display_int(n):
    """displays a text only if it is int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_tmp(n=None):
    """if url contains an integer, renders 5-number_template.html"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """returns an html page of even or odd depending on the iput"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
