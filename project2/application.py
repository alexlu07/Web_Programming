import os
from classes import *
from flask import Flask, request, render_template, redirect, url_for, session
from flask import Flask
from flask import jsonify, json
import requests
import pprint
from flask_socketio import SocketIO, emit, join_room, leave_room

#Flask run --host=192.168.86.35

app = Flask(__name__)
app.config["SECRET_KEY"] = "\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR\xa1\xa8"
socketio = SocketIO(app)

user_derek = all_users.create_user("derek", "123")
user_alex  = all_users.create_user("alex", "123")
user_jun   = all_users.create_user("jun", "123")

channelAlex = "Alex_private"
channelDerek = "Derek_private"
channelJun = "Jun_family"

all_channels.create_channel(channelJun)
all_channels.create_channel(channelAlex)
all_channels.create_channel(channelDerek)
all_channels.create_channel("Nothing")

user_alex.join_channel(channelJun)
user_alex.join_channel(channelAlex)
user_alex.join_channel(channelDerek)
user_derek.join_channel(channelJun)
user_derek.join_channel(channelDerek)
user_jun.join_channel(channelJun)

def get_user():
    username = session["username"]
    return all_users.get_user(username)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    userlist = all_users.get_users()
    user = all_users.get_user(username)
    if not userlist or not user:
        return jsonify({"success": False})
    if user.get_password() != password:
        return jsonify({"success": False})

    session["username"] = username
    return jsonify({"success": True})

    # return redirect(url_for('channels'))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/new", methods=["POST"])
def new():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    userlist = all_users.get_users().keys()

    if password != confirm_password:
        return jsonify({"success": False, "message": "Passwords do not match"})

    if username in userlist:
        return jsonify({"success": False, "message": "Username already taken"})

    all_users.create_user(username, password, all_channels)

    session["username"] = username
    return jsonify({"success": True})

@app.route("/channels")
def channel_list():
    username = session["username"]
    channel_names = get_user().get_channels()
    return render_template("channels.html", username = username, channel_list=channel_names)

@app.route("/join", methods=["POST", "GET"])
def join():
    print(request)
    channel = request.form.get("channel")
    user = get_user()
    print(channel)
    user.join_channel(channel)
    session["channel"] = channel
    return redirect(url_for("room", channel=channel))

@app.route("/search", methods=["POST"])
def search():
    search = request.form.get("search")
    print("search=" + search)

    channel_names = list(all_channels.get_channels())
    results = [x for x in channel_names if search.lower() in x.lower()]

    return jsonify(results = results)

@app.route("/channels/<channel>")
def room(channel):
    return render_template("room.html")

@socketio.on('join')
def on_join():
    username = session['username']
    channel = session['channel']
    join_room(channel)
    emit("joined_channel", username + ' has entered the room.', room=channel)

@socketio.on('leave')
def on_leave():
    username = session['username']
    channel = session['channel']
    emit("left_channel", username + "has left the room", room = channel)
    leave_room(channel)
    session.pop('channel', None)

@socketio.on("return_message")
def append_message(message):
    message = message["message"]
    username = session["username"]
    channel = session["channel"]
    all_channels.get_channel(channel).append_messages(username, message)
    print("username: {}, message: {}, channel: {}".format(username, message, channel))
    emit('append_message', {"message": message, "username": username}, room=channel)

@socketio.on("get_all_messages")
def all_messages():
    channel = session["channel"]
    user_messages = all_channels.get_channel(channel).get_messages()
    users = [ pair[0] for pair in user_messages]
    messages = [ pair[1] for pair in user_messages]

    # pprint.pprint(all_users)
    # pprint.pprint(all_channels)
    emit("all_messages", {"users": users, "messages": messages})
