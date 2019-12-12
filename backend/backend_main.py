import flask
from flask import request
from flask import jsonify
# from flask import send_file
# from flask_mail import Mail
# from flask_mail import Message

import os
from datetime import datetime

import db_interact as db_i
from classes import Message
from security import user_valid


app = flask.Flask(__name__)
db_connection = 'not loaded'


@app.route('/', methods=['GET'])
def def_method():
    return 'Hello world!'


@app.route('/test', methods=['GET'])
def test_method():
    '''
    Test method for checking GET request handling.
    '''
    if 'token' in request.args:
        token = request.args['token']
    else:
        token = 'default token'

    return 'Your token was: {}'.format(token)


# Database connected methods

@app.route('/database/init', methods=['POST'])
def db_init():
    '''
    DB initiation method.
    '''
    response = db_i.db_initialization()
    return response     


@app.route('/database/messages', methods=['GET'])
def db_get_all_messages():
    '''
    Get all messages. DB test method.
    '''
    res = db_i.select_all_messages(db_connection)
    return jsonify(res)


# Message connected methods

@app.route('/message/send', methods=['POST'])
def send_message():

    data = request.args

    if not ('sender' in data) or ('receiver' in data) or ('text' in data):
        return 'Message not correct. Try again.'

    message = Message(data['sender'], data['receiver'], data['text'])
    response = db_i.send_message(message)

    return jsonify(response)


@app.route('/message/receive', methods=['GET'])
def receive_messages():
    return 'Receieve message method'


# User connected methods

@app.route('/user/login', methods=['GET'])
def user_login():
    return 'User login method'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True, port = 8080)
