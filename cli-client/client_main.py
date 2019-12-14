import requests 
import os
import sys

from astropy.table import Table
  

'''
TODO:
    Add logger
'''


url = 'http://127.0.0.1:8080'

# r = requests.get(url = url + path, params = params) 
  
# # data = r.json() 

# print(r.text)


def print_menu(username, update=''):

    menu = '''Hello, {}!
Pick an option:

1: Start chat
2: My chats
3: Users
9: Exit

Press enter to refresh page.
{}
'''.format(username, update)

    print(menu)


def user_login():

    username = input('username: ')
    password = input('password: ')

    params = {
            'username': username,
            'password': password
            } 

    r = requests.post(url = url + '/user/login', params = params) 

    if r.text == 'token':
        return username

    elif r.text == 'Incorrect data.':
        return False

    else:
        return 'Unexpected exception'


def receive_messages():

    r = requests.get(url = url + '/message/receive')

    # TODO: implement this method

    return 'You have new message from {}'.format('oleggr')


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


if __name__ == '__main__':

    os.system('cls')
    username = user_login()

    if username == False:
        print('Data incorrect. Try again.')
        sys.exit()

    elif username == 'Unexpected exception':
        print(username)
        sys.exit()


    while True:

            os.system('cls')
            updates = receive_messages()
            print_menu(username, updates)

            command = input()

            if command == '1':
                os.system('cls')

                print('Select user to chat with:')

                t = get_users_table(get_users())
                print(t)

                receiver_name = input('username: ')

                start_chat(receiver_name)

            elif command == '2':
                os.system('cls')
                chats = get_my_chats(username)
                t = get_chats_table(chats)
                print(t)
                input()

            elif command == '3':
                os.system('cls')
                t = get_users_table(get_users())
                print(t)
                input()

            elif command == '9':
                print('Goodbye)')
                break
