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

0: Send message
1: Check received messages

5: Start chat
6: My chats
7: Users

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


def message_input(message=''):

    print(message)

    lines = []

    while True:

        line = input()

        if line:
            lines.append(line)
        else:
            break

    text = '\n'.join(lines)

    return text


def send_message(sender, receiver, message):

    params = {
            'sender': sender,
            'receiver': receiver,
            'text': message
    }

    r = requests.post(url = url + '/message/send', params = params)

    return r.text


def receive_messages(username):

    params = {'username': username}

    r = requests.get(url = url + '/messages/receive', params = params)

    messages = r.json()
    senders = []

    for message in messages:
        sender = message[1]
        senders.append(sender)

    if len(senders) == 0:
        return ''
    elif len(senders) == 1:
        return '* You have new message from {}'.format(senders[0])
    else:
        return '* You have new messages from {} and {} more'.format(senders[0], len(senders) - 1)


def sortDate(val):
    return val[4]


def check_messages(username):

    params = {'username': username}

    r = requests.get(url = url + '/messages/check', params = params)

    messages = r.json()
    data = []

    messages.sort(key = sortDate)

    for message in messages:
        print(message[1] + '> ' + message[3])


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
