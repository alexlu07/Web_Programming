


class User:
    name = ""
    password = ""

    channels = set()
    current_channel = ""

    def __init__(self, name):
        self.name = name

    def join_channel(self, channel):
        self.channels.add(channel)
        self.current_channel = channel

    def change_channel(self, channel):
        if channel in channels:
            self.current_channel = channel

    def current_channel(self):
        return self.current_channel

    def get_name(self):
        return self.name

    def get_channels(self):
        return self.channels


class Users:
    users = {}

    def create_user(self, name):
        if name in users:
            return False;
        user = User(name)
        self.users[name] = user

    def get_user(self, name):
        if name in self.users:
            return self.users[name]
        else:
            return None

    def get_users(self):
        return self.users


class Channel:
    name = ""
    users = set()
    messages = []

    def __init__(self, name):
        self.name = name

    def add_user(self, user):
        self.users.add(user)

    def get_users(self):
        return self.users

    def append_messages(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

class Channels:
    channels = {}


# from flask_sqlalchemy import SQLAlechemy
#
# db = SQLAlchemy()
#
# class Channel(db.model):
#     __tablename__ = "channels"
#     name = db.Column(db.String, nullable=False)
#     users = db.Column()
