sqlite_create_messages_table_query = '''CREATE TABLE messages (
                                id INTEGER PRIMARY KEY,
                                sender INTEGER NOT NULL,
                                receiver INTEGER NOT NULL,
                                message TEXT NOT NULL,
                                created_at datetime NOT NULL);'''

sqlite_create_users_table_query = '''CREATE TABLE users (
                                id INTEGER PRIMARY KEY,
                                nickname TEXT NOT NULL,
                                password_hash TEXT NOT NULL,
                                created_at datetime NOT NULL);'''

select_all_messages = 'SELECT * FROM messages'
delete_all_messages = 'DELETE FROM messages;'

select_all_messages = 'SELECT * FROM users'