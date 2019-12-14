import sys
import requests


url = 'http://127.0.0.1:8080'


def print_admin_menu():

    menu = '''### ADMIN MODE ###
\"Big power means big responsibility.\" @Uncle Ben

Pick an option:

1: DB init
2: Drop all messages
3: Drop DB
4: See all messages

5: Hello world
6: Test request

Anykey to exit admin mode
'''
    
    print(menu)


def main_admin(command):

    if command == '1':
        return db_init()

    elif command == '2':
        return drop_all_messages()

    elif command == '3':
        print('Are you shure about it?\nApplication will be stopped\nyes/no')
        reply = input()

        if reply == 'yes':
            db_drop()
            sys.exit()

    elif command == '4':
        return see_all_messages()

    elif command == '5':
        return hello_world()

    elif command == '6':
        return test_request()
    
    else:
        return ''


def db_init():
    r = requests.post(url = url + '/database/init')
    return r.text


def drop_all_messages():
    r = requests.post(url = url + '/database/drop/messages')
    return r.text


def db_drop():
    r = requests.post(url = url + '/database/drop')
    return r.text


def see_all_messages():
    r = requests.get(url = url + '/database/messages')
    return r.text


def hello_world():
    r = requests.get(url = url + '/')
    return r.text


def test_request():
    r = requests.get(url = url + '/test')
    return r.text