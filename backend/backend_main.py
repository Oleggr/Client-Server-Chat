import flask
from flask import request
from flask import jsonify
# from flask import send_file
# from flask_mail import Mail
# from flask_mail import Message

import os
import hashlib
from datetime import datetime

import db_interact as db_i
from classes import Message, User, Chat
from security import user_valid


'''
TODO:

    Change names to nicknames.
    Add other classes (User, Chat, Room, etc.)
    Implement methods (Delete message, create user, login user, etc.) 

    Add logger
'''

app = flask.Flask(__name__)


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
    Get all messages. 
    DB test method.
    Will be deleted in final version.
    '''
    res = db_i.select_all_messages()
    return jsonify(res)


@app.route('/database/drop', methods=['POST'])
def drop_db():
    res = db_i.db_drop()
    return res


@app.route('/database/drop/messages', methods=['POST'])
def drop_all_messages():
    res = db_i.drop_all_messages()
    return res


# Message connected methods

@app.route('/message/send', methods=['POST'])
def send_message():

    data = request.args

    if not (('sender' in data) and ('receiver' in data) and ('text' in data)):
        return 'Message not correct. Try again.'

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

    message = Message(data['sender'], data['receiver'], data['text'], dt_string)
    response = db_i.send_message(message)

    return jsonify(response)


@app.route('/message/receive', methods=['GET'])
def receive_messages():

    data = request.args

    if not ('username' in data):
        return 'Requset not correct. Try again.'

    response = db_i.receive_messages(data['username'])

    return 'Receieve message method'


# User connected methods

@app.route('/user/login', methods=['POST'])
def user_login():

    data = request.args
    
    if not (('username' in data) and ('password' in data)):
        return 'User data is not correct. Try again.'

    password = data['password']
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)

    response = db_i.user_login(data['username'], password_hash.hex())

    return response


@app.route('/user/register', methods=['POST'])
def user_register():

    data = request.args
    
    if not (('username' in data) and ('password' in data)):
        return 'User data is not correct. Try again.'

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

    password = data['password']
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)

    user = User(data['username'], password_hash.hex(), dt_string)
    response = db_i.user_create(user)

    if response == 'User exist. Try another username.':
        return response
    else:
        return jsonify(response)


@app.route('/users', methods=['GET'])
def get_all_users():
    '''
    Get all messages. DB test method.
    '''
    res = db_i.select_all_users()
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True, port = 8080)
