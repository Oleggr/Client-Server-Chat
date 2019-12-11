import sqlite3

def db_initialization():

    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        sqlite_create_table_query = '''CREATE TABLE messages (
                                    id INTEGER PRIMARY KEY,
                                    sender INTEGER NOT NULL,
                                    receiver INTEGER NOT NULL,
                                    message TEXT NOT NULL,
                                    joining_date datetime);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        cursor.execute(sqlite_create_table_query)

        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

        return "OK"

    except sqlite3.Error as error:
        return "Error while connecting to sqlite {}".format(error)
        
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            return "The SQLite connection is closed"