import flask
from flask import request
from flask import send_file
from flask import jsonify
from flask_mail import Mail
from flask_mail import Message

import os
from datetime import datetime


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def def_method():
    return 'Hello world!'


@app.route('/test', methods=['GET'])
def test_method():
    '''
    Test method for checking GET request handling.
    '''
    token = request.args["token"]
    return token + 'aaaa'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True, port = 8080)
