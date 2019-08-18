
import pprint

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

    def append_messages(self, username, message):
        self.messages.append([username, message])

    def get_messages(self):
        return self.messages

    def get_name(self):
        return self.name

    def __repr__(self):
        result = {
        "channel": self.name,
        "users" : self.users,
        "messages": self.messages,
        }
        return pprint.pformat(result) + "\n"

    def __str__(self):
        return pprint.pformat(self.__repr__())

class Channels:
    channels = {}

    def create_channel(self, name):
        if name in self.channels.keys():
            return False
        channel = Channel(name)
        self.channels[name] = channel

    def get_channel(self, name):
        if name in self.channels.keys():
            return self.channels[name]
        else:
            return None

    def get_channels(self):
        return self.channels.keys()

    def __repr__(self):
        result = { "channels": self.channels }
        return pprint.pformat(result) + "\n"

    def __str__(self):
        return pprint.pformat(self.__repr__())

all_channels = Channels()

class User:
    name = ""
    password = ""
    channels = set()

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def join_channel(self, channel):
        self.channels.add(channel)
        all_channels.get_channel(channel).add_user(self.name)

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_channels(self):
        return self.channels

class Users:
    users = {}

    def create_user(self, name, password):
        if name in self.users.keys():
            return None;
        user = User(name, password)
        self.users[name] = user
        return user

    def get_user(self, name):
        if name in self.users:
            return self.users[name]
        else:
            return None

    def get_users(self):
        return self.users

all_users = Users()
