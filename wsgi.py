#!/usr/bin/env python3

from flask import Flask, escape, request

application = Flask(__name__)


@application.route("/")
def hello():
    name = request.args.get("name", "World")
    return {"msg": "Hello, {}!".format(escape(name))}


if __name__ == "__main__":
    application.run()
