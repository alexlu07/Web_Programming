


class User:
    name = ""
    password = ""

    channels = set()

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def join_channel(self, channel):
        self.channels.add(channel)
        self.current_channel = channel

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
            return False;
        user = User(name, password)
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

    def get_name(self):
        return self.name

class Channels:
    channels = {}
    bob = Channel("bob")
    channels["bob"] = bob
    print(channels)

    def create_channel(self, name):
        if name in self.channels.keys():
            return False
        channel = Channel(name)
        self.channels[name] = channel

    def get_channel(self, name):
        if name in self.channels:
            return self.channels[name]
        else:
            return None

    def get_channels(self):
        return self.channels.keys()
