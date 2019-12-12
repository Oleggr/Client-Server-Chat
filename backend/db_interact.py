import sqlite3

import db_queries as db_q


def db_initialization():

    try:
        sqliteConnection = sqlite3.connect('sqlite.db')
        
        cursor = sqliteConnection.cursor()
        cursor.execute(db_q.sqlite_create_table_query)
        
        sqliteConnection.commit()

        cursor.close()
        sqliteConnection.close()

        return 'OK'

    except sqlite3.Error as error:
        return 'Error while connecting to sqlite {}'.format(error)


def send_message(message):

    return {'sender': message.sender,
            'receiver': message.receiver,
            'text': message.text}


def select_all_messages():

    try:
        sqliteConnection = sqlite3.connect('sqlite.db')

        cur = sqliteConnection.cursor()
        cur.execute("SELECT * FROM messages")
     
        rows = cur.fetchall()
        res = []
     
        for row in rows:
            res.append(row)

        sqliteConnection.close()

        return res

    except Exception as e:
        return "Error while getting messages {}".format(e)


def db_test_data_load():
    pass