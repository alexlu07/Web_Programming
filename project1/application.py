import os
import csv
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

def select(target, table, input, info):
    return db.execute("SELECT {} FROM {} WHERE {} = '{}';"
    .format(target, table, input, info)).fetchone()

@app.route("/")
def index():
    #read csv file
    f = open("books.csv")
    reader = csv.reader(f)
    number_books = db.execute("SELECT * FROM books;").fetchall()
    if number_books == []:
        for isbn, title, author, year in reader:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
            {"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()

    session["user_id"] = None
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
    result = db.execute("SELECT * FROM login WHERE username = '{username}' AND password = '{password}' "
    .format(username = username, password = password)).fetchall()
    if len(result) == 0:
        message = "Username and/or Password is incorrect!"
        # session["message"] = message
        # return redirect(url_for("index"))
        return redirect(url_for("index", message = message))
    else:
        row = select("id", "login", "username", username)
        session["user_id"] = row[0]
        return redirect(url_for("success"))

@app.route("/dashboard", methods=['GET', 'POST'])
def success():
    #get username
    row = select("username", "login", "id", session["user_id"])
    username = row[0]

    methods = request.form.get('search_methods')
    search = request.form.get('search')


    if methods in ("author", "title"):
        methods = "UPPER({})".format(methods)
        search = search.upper()

    books = []
    if methods and search:
        db_str = "SELECT * FROM books WHERE {methods} LIKE '%{search}%';".format(
            methods = methods, search = search)
        print(db_str)
        books = db.execute(db_str).fetchall()
    return render_template("success.html", username = username, books = books)

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

    taken_usernames = db.execute("SELECT username FROM login").fetchall()
    for x in taken_usernames:
        if new_username == x[0]:
            message = "Username already taken"
            return redirect(url_for("register", message = message))

    if new_password == confirm_password:
        db.execute("INSERT INTO login(username, password) VALUES('{username}', '{password}')"
        .format(username = new_username, password = new_password))
        db.commit()
        row = select("id", "login", "username", new_username)
        session["user_id"] = row[0]
        return redirect(url_for("success"))

    message = "Passwords do not match."
    return redirect(url_for("register", message = message))
