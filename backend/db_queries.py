sqlite_create_messages_table_query = '''CREATE TABLE messages (
                                id INTEGER PRIMARY KEY,
                                sender INTEGER NOT NULL,
                                receiver INTEGER NOT NULL,
                                message TEXT NOT NULL,
                                created_at datetime NOT NULL,
                                is_checked BOOLEAN NOT NULL);'''

select_all_messages = 'SELECT * FROM messages'
delete_all_messages = 'DELETE FROM messages;'


sqlite_create_users_table_query = '''CREATE TABLE users (
                                id INTEGER PRIMARY KEY,
                                username TEXT NOT NULL,
                                password_hash TEXT NOT NULL,
                                created_at datetime NOT NULL);'''

select_all_users = 'SELECT id, username, created_at FROM users;'


sqlite_create_chats_table_query = '''CREATE TABLE chats (
                                id INTEGER PRIMARY KEY,
                                username1 TEXT NOT NULL,
                                username2 TEXT NOT NULL,
                                created_at datetime NOT NULL,
                                is_group BOOLEAN NOT NULL);'''

select_all_chats = 'SELECT * FROM chats'
