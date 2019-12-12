sqlite_create_table_query = '''CREATE TABLE messages (
                                id INTEGER PRIMARY KEY,
                                sender INTEGER NOT NULL,
                                receiver INTEGER NOT NULL,
                                message TEXT NOT NULL,
                                joining_date datetime);'''
        