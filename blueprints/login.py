from flask import Flask, Blueprint, request, session, render_template, flash, redirect
from cs50 import SQL
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__, template_folder='templates')

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memories.db")

@login_bp.route('/login', methods=["GET", "POST"])
def login():
    """Log user in"""

    session["username"] = request.form.get("username")
    
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        session["username"] = request.form.get("username")
        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("un_auth/pages/login.html" , error="Username is required")

        # Ensure password was submitted
        elif not request.form.get("password"):
          return render_template("un_auth/pages/login.html", error="Password is required")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE user_username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["user_password"], request.form.get("password")
        ):
          return render_template("un_auth/pages/login.html", error = "Invalid username or password!")

        # Remember which user has logged in
        if 'user_id' not in session:
          session["user_id"] = rows[0]["user_id"]
        if 'username' not in session:
          session["username"] = rows[0]["user_username"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("un_auth/pages/login.html")