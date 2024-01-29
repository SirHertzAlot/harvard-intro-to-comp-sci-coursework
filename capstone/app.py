import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memories.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log the user in"""

    session["name"] = request.form.get("username")

    #Forget user id
    session.clear()

    #Log user in if user is posting to service
    if request.method == "POST":
        session["name"] = request.form.get("username")
        if not request.form.get("user"):
            return apology("Please provide a username", 403)

        elif not request.form.get("password"):
            return apology("Please enter your password", 403)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("Please check your username or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:

        return render_template("login.html")

@app.route("/logout")
def logout():
    """ Log user out """

    session.clear()

    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if password == confirmation and len(password) > 0 and len(username) > 0:
            hash = generate_password_hash(password)
            try:
                db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
            except:
                return apology("Username is already in use", 400)
        elif len(password.strip()) == 0 or len(username.strip()) == 0:
            return apology("Username or password cannot be blank.", 400)
        elif password != confirmation:
            return apology("Password does not match.", 400)
        else:
            return apology("Username or password is invalid.", 400)
    else:
        return render_template("register.html")

    return redirect("/login")


