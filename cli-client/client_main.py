import requests 
import os

from astropy.table import Table
  

url = 'http://127.0.0.1:8080'

# r = requests.get(url = url + path, params = params) 
  
# # data = r.json() 

# print(r.text)


def print_menu():

    menu = '''Hello, user!
Pick an option:

1: Start chat
2: Users
3: Exit
'''

    print(menu)


def user_login():
    params = {'token': 'bbb'} 
    r = requests.get(url = url + '/user/login', params = params) 
    data = r.json()


def get_users():

    r = requests.get(url = url + '/users') 
    data = r.json()

    return data


def get_users_table(users):
    t = Table(names=('id', 'username', 'created at'), dtype=('i4', 'S', 'S'))

    for elem in users:
        t.add_row((elem[0], elem[1], elem[2]))


if __name__ == '__main__':

    while True:

        os.system('cls')
        username = user_login()

        os.system('cls')
        print_menu()

        command = input()

        if command == '1':
            os.system('cls')

            print('Select user to chat with:')

            t = get_users_table(get_users())
            print(t)

            user_id = input('User id: ')

        elif command == '2':
            os.system('cls')
            t = get_users_table(get_users())
            print(t)
            input()

        elif command == '3':
            print('Goodbye)')
            break

