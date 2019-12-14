import sqlite3

import db_queries as db_q


def db_initialization():

    try:
        sqliteConnection = sqlite3.connect('sqlite.db')
        
        cursor = sqliteConnection.cursor()
        cursor.execute(db_q.sqlite_create_messages_table_query)
        cursor.execute(db_q.sqlite_create_users_table_query)
        cursor.execute(db_q.sqlite_create_chats_table_query)

        sqliteConnection.commit()

        cursor.close()
        sqliteConnection.close()

        return 'OK'

    except sqlite3.Error as error:
        return 'Error while connecting to sqlite {}'.format(error)


def send_message(message):

    sqliteConnection = sqlite3.connect('sqlite.db')

    cursor = sqliteConnection.cursor()
    cursor.execute(message.set_message_sql_query, (message.sender, message.receiver, message.text, message.created_at))

    sqliteConnection.commit()

    cursor.close()
    sqliteConnection.close()

    reply = {'sender': message.sender,
            'receiver': message.receiver,
            'text': message.text,
            'created_at': message.created_at}

    return reply


def select_all_messages():

    try:
        sqliteConnection = sqlite3.connect('sqlite.db')

        cur = sqliteConnection.cursor()
        cur.execute(db_q.select_all_messages)
     
        rows = cur.fetchall()
        res = []
     
        for row in rows:
            res.append(row)

        sqliteConnection.close()

        return res

    except Exception as e:
        return "Error while getting messages {}".format(e)


def drop_all_messages():

    try:
        sqliteConnection = sqlite3.connect('sqlite.db')

        cursor = sqliteConnection.cursor()
        cursor.execute(db_q.delete_all_messages)
     
        sqliteConnection.commit()

        cursor.close()
        sqliteConnection.close()

        return 'All messages was deleted'

    except Exception as e:
        return "Error while deleting messages {}".format(e)


def select_all_users():

    try:
        sqliteConnection = sqlite3.connect('sqlite.db')

        cur = sqliteConnection.cursor()
        cur.execute(db_q.select_all_users)
     
        rows = cur.fetchall()
        res = []
     
        for row in rows:
            res.append(row)

        sqliteConnection.close()

        return res

    except Exception as e:
        return "Error while getting users {}".format(e)


def db_test_data_load():
    pass