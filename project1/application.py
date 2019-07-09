import os
from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.secret_key = "wsb@e7$%wgf44VRrNA*&Nk^DzAV$QL"
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    # if "message" in session:
    #     message = session["message"]
    # else:
    #     message = ""
    # return render_template("login.html", message = message)
    message = ""
    if "message" in request.args:
        message = request.args["message"]
    return render_template("login.html", message = message)

@app.route("/login", methods=['POST']) #, 'POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    result = db.execute("SELECT * FROM login WHERE username = username AND password = password").fetchall()
    if not result:
        message = "Username and/or Password is incorrect!"
        # session["message"] = message
        # return redirect(url_for("index"))
        return redirect(url_for("index", message = message))
    else:
        return redirect(url_for("success"))

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/register")
def register():
    message = ""
    if "message" in request.args:
        message = request.args["message"]
    return render_template("register.html", message = message)

@app.route("/insert", methods=['POST'])
def insert():
    new_username = request.form.get("username")
    new_password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if new_password == confirm_password:
        db.execute("INSERT INTO login (username, password) VALUES ('{username}', '{password}'); "
        .format(username=new_username, password=new_password))
        db.commit()

        return redirect(url_for("success"))
    message = "Passwords do not match."
    return redirect(url_for("register", message = message))
