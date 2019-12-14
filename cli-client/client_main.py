import os
import sys

import user_functions as uf
import admin_functions as af
  

'''
TODO:
    Add logger
    Implement receive_messages method
'''

# r = requests.get(url = url + path, params = params) 
# # data = r.json() 
# print(r.text)

if __name__ == '__main__':

    os.system('cls')
    uf.hello_screen()
    choise = input()

    if choise == '1':

        # Login
        os.system('cls')
        response = uf.user_login()

        if response == False:
            print('Data incorrect. Try again.')
            sys.exit()

        username, user_id = response[0], response[1]

    elif choise == '2':

        # Register and login after it
        os.system('cls')
        response = uf.user_register()
        print(response)

        if response == 'User exist. Try another username.':
            sys.exit()

        os.system('cls')
        response = uf.user_login()

        if response == False:
            print('Data incorrect. Try again.')
            sys.exit()

        username, user_id = response[0], response[1]

    else:
        sys.exit()


    while True:

        os.system('cls')
        updates = uf.receive_messages(username)
        uf.print_menu(username, updates)

        command = input()


        if command == '1':

            # Start chat
            os.system('cls')
            print('Select user to chat with:')

            t = uf.get_users_table(uf.get_users())
            print(t)

            receiver_name = input('username: ')

            uf.start_chat(sender, receiver_name)


        elif command == '2':

            # Show my chats
            os.system('cls')
            chats = uf.get_my_chats(username)
            t = uf.get_chats_table(chats)
            print(t)
            input()


        elif command == '3':

            # Show users
            os.system('cls')
            t = uf.get_users_table(uf.get_users())
            print(t)
            input()


        elif command == '8':
            os.system('cls')

            print('Login page\n')
            username = input('username: ')
            password = input('password: ')

            if username == 'oleggr' and password == '1235':

                while True:
                    os.system('cls')
                    af.print_admin_menu()
                    admin_command = input()

                    if admin_command in '123456':
                        res = af.main_admin(admin_command)
                        print(res)
                        input()

                    else:
                        print('Bye')
                        input()
                        break
                
            else:
                print('Incindent will be reported.')
                input()
                sys.exit()
                

        elif command == '9':
            print('Goodbye)')
            break
