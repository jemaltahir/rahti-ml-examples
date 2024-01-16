#!/usr/bin/env python3

from flask import Flask, request
from werkzeug.utils import escape

application = Flask(__name__)


@application.route("/")
def hello():
    name = request.args.get("name", "World")
    return {"msg": "Hello, {}!".format(escape(name))}


if __name__ == "__main__":
    application.run()
