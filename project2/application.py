import os
import classes
from flask import Flask, request, render_template, redirect, url_for, session
from flask import Flask
from flask import jsonify
import requests
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = classes.Users()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    userlist = users.get_users()
    return jsonify({"users": userlist})
