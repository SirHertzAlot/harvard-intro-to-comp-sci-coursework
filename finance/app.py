import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is my key'

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

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
    try:
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            portfolio = db.execute("SELECT * FROM portfolio WHERE UserId = ?", session["user_id"])
    except:
        return apology("Account does not exist.", 400)
    return render_template("portfolio.html", results=portfolio, balance=cash)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    """Buy shares of stock"""
    if request.method == "POST":

        if len(request.form.get("symbol")) < 1:
            return apology("Stock not found", 400)
        else:
            product = request.form.get("symbol")

        if request.form.get("shares").isdigit() and int(request.form.get("shares")) > 0:
            shares = request.form.get("shares")
        else:
            return apology("Please enter amount greater than 0", 400)


        try:
            stats = lookup(product)
            price = stats["price"]
        except:
            return apology("Ticker symbol is not valid.", 400)

        totalPrice = price * float(shares)

        try:
            username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
        except:
            return apology("Account does not exist.", 400)

        try:
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        except:
            return apology("Account does not exist.", 400)

        funds = float(cash[0].get("cash"))

        if funds > totalPrice:
            #Get user's portfolio
            portfolio = db.execute("SELECT * FROM portfolio WHERE UserId = ?", session["user_id"])
            #Check if stock is in portfolio
            if portfolio:
                if portfolio[0].get("symbol") == product:
                    #Update portfolio since stock is present
                    db.execute("UPDATE portfolio SET amount = (amount + ?) WHERE UserId = ?", shares, session["user_id"])
                    #Update cash spent during transaction
                    db.execute("UPDATE users SET cash = (SELECT ? - ? FROM users WHERE id = ?)", funds, totalPrice, session["user_id"])
                    #INSERT INTO TRANSACTIONS TABLE
                    db.execute("INSERT INTO transactions (username, symbol, price, UserId) VALUES (?,?,?,?)", username[0].get("username"), request.form.get("symbol"), totalPrice, session["user_id"])
                    return redirect("/")
            else:
                #Only runs if there is a new stock present that user doesn't already own.
                db.execute("INSERT INTO portfolio (username, symbol, amount, UserId , price_per_share) VALUES (?,?,?,?,?)", username[0].get("username"), request.form.get("symbol"), shares, session["user_id"], stats["price"])
                #Update cash spent during transaction
                db.execute("UPDATE users SET cash = (SELECT ? - ? FROM users WHERE id = ?)", funds, totalPrice, session["user_id"])
                #INSERT INTO TRANSACTIONS TABLE
                db.execute("INSERT INTO transactions (username, symbol, price, UserId) VALUES (?,?,?,?)", username[0].get("username"), request.form.get("symbol"), totalPrice, session["user_id"])
                return redirect("/")
        else:
            return apology("Please add more cash or sell some stock to perform this transaction.", 400)
    else:
        return render_template("buy.html")

    return apology("TODO")


@app.route("/history")
@login_required
def history():

    try:
        results = db.execute("SELECT * FROM transactions WHERE id = ? AND SELECT price_per_share FROM portfolio WHERE id = ?", session["user_id"], session["user_id"])
    except:
        return render_template("history.html")

    return render_template("history.html", results=results)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session["name"] = request.form.get("username")

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        session["name"] = request.form.get("username")
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":

        symbol = request.form.get("symbol")

        try:
            if symbol:
                results = lookup(symbol)
                return render_template("quoted.html", results=results)
            else:
              return apology("Ticker symbol cannot be blank", 400)
        except:
            return apology("Ticker symbol does not exist", 400)

    else:
        return render_template("quote.html")


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


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":

        if request.form.get("symbol") == " ":
            return apology("Stock not found", 400)
        else:
            symbols = db.execute("SELECT symbol FROM portfolio WHERE UserId = ?", session["user_id"])

            shares = db.execute("SELECT amount FROM portfolio WHERE UserId = ? AND symbol = ?", session["user_id"], request.form.get("symbol"))

            if request.form.get("shares").isnumeric and int(request.form.get("shares")) > 1:
                if shares:
                    if shares > int(request.form.get("shares")):
                        stats = lookup(stock.get("symbol"))
                        price = stats["price"]

                        totalPrice = price * float(int(request.form.get("shares")))

                        cash = db.execute("SELECT cash FROM users WHERE UserId = ?", session["user_id"])

                        username = db.execute("SELECT username FROM users WHERE UserId = ?", session["user_id"])

                        funds = float(cash[0].get("cash"))

                        db.execute("UPDATE users SET cash = (SELECT ? + ? FROM users WHERE UserId = ?)", funds, totalPrice, session["user_id"])
                        #INSERT INTO TRANSACTIONS TABLE
                        db.execute("INSERT INTO transactions (username, symbol, price, UserId) VALUES (?,?,?,?)", username[0].get("username"), request.form.get("symbol"), totalPrice, session["user_id"])
                        db.execute("UPDATE transactions SET purchase_status = (? WHERE UserId = ?)",'sold', session["user_id"])
                        #INSERT INTO PORTFOLIO TABLE
                        db.execute("DELETE FROM portfolio WHERE UserId= ? and symbol = ?", session["user_id"], request.form.get("symbol"))
                    else:
                        return apology("Make sure you have enough shares of this stock to sell first.", 400)
                else:
                    return apology("Please buy some stocks to sell first.", 400)
            else:
                return apology("Please enter valid share amount", 400)
            return redirect("/")
    else:
        symbols = db.execute("SELECT * FROM portfolio WHERE UserId = ?", session["user_id"])
        if symbols:
            return render_template("sell.html", symbols=symbols)
        return render_template("sell.html")


@app.route("/update", methods=["GET", "POST"])
@login_required
def update():
    if request.method == "POST":
        new_val = request.form.get("update")
        if len(new_val) > 1:
            hashed_val = generate_password_hash(new_val)
            db.execute("UPDATE users SET hash = ? WHERE id = ?", hashed_val, session["user_id"])
            return redirect("/")
    else:
        return render_template("update.html")
