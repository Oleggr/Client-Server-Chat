sqlite_create_table_query = '''CREATE TABLE messages (
                                id INTEGER PRIMARY KEY,
                                sender INTEGER NOT NULL,
                                receiver INTEGER NOT NULL,
                                message TEXT NOT NULL,
                                created_at datetime);'''

select_all_messages = 'SELECT * FROM messages'
delete_all_messages = 'DELETE FROM messages;'