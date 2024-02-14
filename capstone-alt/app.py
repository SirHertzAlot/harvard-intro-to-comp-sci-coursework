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

@app.route("/api/getcal")
def getCalView():
    new_cal = calendar.HTMLCalendar(firstweekday=0)
    formatted_cal = str(new_cal.formatyear(curr_year))
    month_view = new_cal.formatmonth(curr_year, curr_month)
    return render_template("pages/index.html", new_cal=month_view)

@app.route("/api/day")
def getDayView():
    hours = genHours()
    return render_template("pages/index.html", new_day=month_view)
