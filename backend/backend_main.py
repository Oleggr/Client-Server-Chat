import flask
from flask import request
from flask import jsonify
# from flask import send_file
# from flask_mail import Mail
# from flask_mail import Message

import os
from datetime import datetime

from security import user_valid
from db_interact import db_initialization


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
    return 'Your token was: {}'.format(token)


@app.route('/database/init', methods=['POST'])
def db_init():
    '''
    DB initiation method
    '''
    return db_initialization()


# Message connected methods

@app.route('/message/send', methods=['POST'])
def send_message():
    return 'Send message method'


@app.route('/message/receive', methods=['GET'])
def receive_messages():
    return 'Receieve message method'


# User connected methods

@app.route('/user/login', methods=['GET'])
def user_login():
    return 'User login method'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True, port = 8080)
