class Message():

    set_message_sql_query = 'INSERT INTO messages (sender, receiver, message, created_at) VALUES (?, ?, ?, ?)'

    def __init__(self, sender, receiver, text, created_at):
        self.sender = sender
        self.receiver = receiver
        self.text = text
        self.created_at = created_at

    # sender = ''
    # receiver = ''
    # text = ''

    