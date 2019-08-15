import os
import classes
from flask import Flask, request, render_template, redirect, url_for, session
from flask import Flask
from flask import jsonify, json
import requests
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR\xa1\xa8"
socketio = SocketIO(app)

users = classes.Users()
channels = classes.Channels()

users.create_user("bob", "123")
channels.create_channel("bobsayshi")
users.get_user("bob").join_channel("bobsayshi")
channels.get_channel("bobsayshi").add_user("bob")


def get_user():
    username = session["username"]
    return users.get_user(username)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    userlist = users.get_users()
    user = users.get_user(username)
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
    userlist = users.get_users().keys()

    if password != confirm_password:
        return jsonify({"success": False, "message": "Passwords do not match"})

    if username in userlist:
        return jsonify({"success": False, "message": "Username already taken"})

    users.create_user(username, password)

    session["username"] = username
    return jsonify({"success": True})

@app.route("/channels")
def channel_list():
    username = session["username"]
    channel_names = channels.get_channels()
    return render_template("channels.html", username = username, channel_list=channel_names)

@app.route("/join", methods=["POST", "GET"])
def join():
    print(request)
    channel = request.form.get("channel")
    user = get_user()
    user.join_channel(channel)
    return redirect(url_for("room", channel=channel))

@app.route("/search", methods=["POST"])
def search():
    search = request.form.get("search")
    print("search=" + search)

    channel_names = list(channels.get_channels())
    results  = [x for x in channel_names if search in x]
    print(results)
    return jsonify(results = results)

@app.route("/channel/<channel>")
def room(channel):
    messages = channels.get_channel(channel).get_messages()
    print(messages)
    return render_template("room.html", messages = messages)
