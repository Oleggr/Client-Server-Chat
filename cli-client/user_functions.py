import requests
from astropy.table import Table


url = 'http://127.0.0.1:8080'


def hello_screen():

    hello_screen = '''1: Login
2: Register
3: Exit'''

    print(hello_screen)


def print_menu(username, update=''):

    menu = '''Hello, {}!
Pick an option:

1: Start chat
2: My chats
3: Users

8: Become admin
9: Exit

Press enter to refresh page.
{}
'''.format(username, update)

    print(menu)


def user_register():

    print('Registration page\n')

    username = input('username: ')
    password = input('password: ')

    params = {
            'username': username,
            'password': password
            } 

    r = requests.post(url = url + '/user/register', params = params) 

    return r.text


def user_login():

    print('Login page\n')

    username = input('username: ')
    password = input('password: ')

    params = {
            'username': username,
            'password': password
            } 

    r = requests.post(url = url + '/user/login', params = params) 

    if ' ' in r.text:
        return False

    return username, r.text


def receive_messages(username):

    params = {'username': username}

    r = requests.get(url = url + '/message/receive', params = params)

    # TODO: implement this method

    return '* You have new message from {}'.format('oleggr')


def get_users():

    r = requests.get(url = url + '/users') 
    data = r.json()

    return data


def get_users_table(users):
    t = Table(names=('id', 'username', 'created at'), dtype=('i4', 'S', 'S'))

    for elem in users:
        t.add_row((elem[0], elem[1], elem[2]))

    return t


def get_chats_table(chats):
    t = Table(names=('username1', 'username2', 'created at', 'is group chat'), dtype=('i4', 'S', 'S', 'S'))

    for elem in chats:
        t.add_row((elem[0], elem[1], elem[2], elem[3]))

    return t


def get_my_chats(username):
    pass


def start_chat(sender, receiver):
    pass
