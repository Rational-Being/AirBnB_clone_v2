#!/usr/bin/python3
"""
a flsk script that starts a flask web application listening on
0.0.0.0 port 5000
"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
