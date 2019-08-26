
import pprint

class Channel:
    def __init__(self, name):
        self.name = name
        self.users = set()
        self.messages = []
        self.active_users = set()

    def add_user(self, user):
        #print("channel: {} add user {}".format(self.name, user))
        self.users.add(user)

    def get_users(self):
        return self.users

    def append_messages(self, username, message):
        self.messages.append([username, message])

    def get_messages(self):
        return self.messages

    def get_name(self):
        return self.name

    def set_active_user(self, user, active):
        if user in self.users:
            if active:
                self.active_users.add(user)
            else:
                self.active_users.remove(user)

    def get_active_users(self):
        return self.active_users

    def __repr__(self):
        result = {
        "channel_name": self.name,
        "users" : self.users,
        "messages": self.messages,
        }
        return pprint.pformat(result) + "\n"

    def __str__(self):
        return pprint.pformat(self.__repr__())

class Channels:
    def __init__(self):
        self.channels = {}

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

    def join_channel(self, username, channel_name):
        # import pdb; pdb.set_trace()
        if channel_name in self.channels.keys():
            self.channels[channel_name].add_user(username)

    def get_channels(self):
        return self.channels.keys()

    def __repr__(self):
        result = { "channels": self.channels }
        return pprint.pformat(result) + "\n"

    def __str__(self):
        return pprint.pformat(self.__repr__())

all_channels = Channels()

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.channels = set()

    def join_channel(self, channel):
        #print("user: {} add channel {}".format(self.name, channel))
        self.channels.add(channel)
        all_channels.join_channel(self.name, channel)

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_channels(self):
        return self.channels

    def __repr__(self):
        result = {
            "username": self.name,
            "channels": self.channels
             }
        return pprint.pformat(result) + "\n"

    def __str__(self):
        return pprint.pformat(self.__repr__())

class Users:
    def __init__(self):
        self.users = {}

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

    def __repr__(self):
        result = { "Users": self.users }
        return pprint.pformat(result) + "\n"

    def __str__(self):
        return pprint.pformat(self.__repr__())

all_users = Users()
