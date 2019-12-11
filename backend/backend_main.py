import flask
from flask import request
from flask import send_file
from flask import jsonify
from flask_mail import Mail
from flask_mail import Message

import os
from datetime import datetime


def app_create():
    app = flask.Flask(__name__)
    return app


if __name__ == "__main__":
    app = app_create()
    app.run(host='0.0.0.0', debug = True, port = 8080)
