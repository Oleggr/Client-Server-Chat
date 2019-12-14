class Message():

    set_message_sql_query = 'INSERT INTO messages (sender, receiver, message, created_at) VALUES (?, ?, ?, ?)'

    def __init__(self, sender, receiver, text, created_at):
        self.sender = sender
        self.receiver = receiver
        self.text = text
        self.created_at = created_at
        self.is_checked = False


class User():

    set_user_sql_query = 'INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)'

    def __init__(self, username, password_hash, created_at):
        self.username = username
        self.password_hash = password_hash
        self.created_at = created_at


class Chat():

    create_chat_sql_query = 'INSERT INTO chats (username1, username2, created_at, is_group) VALUES (?, ?, ?, ?)'

    def __init__(self, username1, username2, created_at, is_group):
        self.username1 = username1
        self.username2 = username2
        self.created_at = created_at
        self.is_group = is_group
    