from flask import Flask, render_template
from helpers import genHours
import calendar
from datetime import date

#Configure application
app = Flask(__name__)

curr_day = date.today()
curr_month = curr_day.month
curr_year = curr_day.year

@app.route("/")
def index():
    return render_template("pages/index.html")
