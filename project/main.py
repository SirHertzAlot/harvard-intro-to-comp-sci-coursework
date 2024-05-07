from flask import Flask, render_template, request, Response, session, redirect
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import addOneEvent, searchOneEvent, getMonth, getCalendar, getHours, getThemes, getAllEvents, getWeeks, gotoWeek, getDays, deleteOneEvent, addUser, getUser, login_required
from datetime import datetime
import json

#Configure application
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'super secret key'
Session(app)

@app.route("/")
@login_required
def index():
    if session:
      name = session.get("name")
      
    month = datetime.now().month
    response = getCalendar(month)
    events = getAllEvents(session.get("email"))
    themes = getThemes()
    if response is None:
      return Response(render_template("/pages/error.html"), status=404)
    else:
      return Response(render_template("components/full_cal/cal.html", themes=themes, month=str(month), response=response, name=name, json_events=events), status=200, mimetype='text/html')

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    user = {}
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")
    name = request.form.get("name")
    
    if password != confirm_password:
      message = "Passwords must match"
      return Response(render_template("/pages/register.html", message=message), status=500)
    elif len(password) <= 8:
      message = "Password must be at least 8 characters"
      return Response(render_template("/pages/register.html", message=message), status=500)
    else:
      hashed_password = generate_password_hash(password)
      user["password"] = hashed_password
      user["name"] = name
      user["email"] = email
      message = "Registration successful"
      addUser(user)
      return Response(render_template("pages/login.html", message=message), status=200, mimetype='text/html')
    return render_template("/pages/register.html", message=message)
  elif request.method == "GET":
    return render_template("pages/register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = {}
        email = request.form.get("email")
        password = request.form.get("password")
        
        user["email"] = email
        user["password"] = password
      
        user_account = getUser(user)
      
        if user_account:
          if check_password_hash(user_account["password"], password):
            session["status"] = "Logged in!"
            session["email"] = user_account.get("email")
            session["name"]  = user_account.get("name")
            name = session.get("name")
            return redirect("/")
        else:
            message = "Invalid email or password"
            return render_template("pages/login.html", message=message)
    else:
      return render_template("pages/login.html")
    return render_template("/pages/login.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect("/login")

@app.route("/daysView")
@login_required
def daysView():
  dates = []
  days = getDays()
  months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep', 'Oct', 'Nov', 'Dec']
  year = datetime.now().year
  month = months[datetime.now().month - 1]
  day = datetime.now().day - 1
  hours = getHours()
  events = getAllEvents(session.get("email"))
  for date in days:
    if date[1] == month: 
      dates.append(date[2])
  if request.args.get('today') and request.args.get('a') == 'yesterday':
    year = datetime.now().year
    day = request.args.get('today')
    hours = getHours()
    events = getAllEvents(session.get("email"))
    month = request.args.get('month')
    response = getCalendar(month)
    return Response(render_template("components/day_cal/day_view.html", response=response, month=month,day=str(day), year=year, hours=hours, json_events=events), status=200, mimetype='text/html')
  else:
    if request.args.get('month') or request.args.get('today'):
      response = getCalendar(month)
      month = request.args.get('month')
      day = request.args.get('today')
    else:
      response = getCalendar(month)
      month = months[datetime.now().month - 1]
      day = datetime.now().day - 1
    return render_template("components/day_cal/day_view.html", response=response, month=month, day=str(day), year=year, hours=hours, json_events=events)
  return Response(render_template("components/day_cal/day_view.html", response=response, month=month, day=str(day), year=year, hours=hours, json_events=events), status=200, mimetype='text/html')

@app.route("/weeksView")
@login_required
def weeksView():
  months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep', 'Oct', 'Nov', 'Dec']
  month = months[datetime.now().month - 1]
  year = datetime.now().year
  today = str(datetime.now().day)
  response = getMonth(month)
  
  if request.args.get('nextweek'):
    month = request.args.get('nextmonth')
    today = request.args.get('nextweek')
    week = gotoWeek(month, str(today))
    hours = getHours()
    events = getAllEvents(session.get("email"))
    return Response(render_template("components/week_cal/weeks.html", response=response, hours=hours, week=week, json_events=events,  month=month, year=year), status=200, mimetype='text/html')
  else:
    response = getMonth(month)
    week = gotoWeek(month, today)
    hours = getHours()
    events = getAllEvents(session.get("email"))
    return Response(render_template("components/week_cal/weeks.html", week=week, response=response, hours=hours, json_events=events, month=month, year=year), status=200, mimetype='text/html')

  if request.args.get('nextmonth') and request.args.get('nextweek'):
    today = request.args.get('nextweek')
    month = request.args.get('nextmonth')
    year = datetime.now().year
    week = gotoWeek(month,today)
    hours = getHours()
    events = getAllEvents(session.get("email"))
    response = getMonth(month)
    return Response(render_template("components/week_cal/weeks.html", response=response, hours=hours, week=week, json_events=events,  month=month, year=year), status=200, mimetype='text/html')

@app.route("/api/calendarView")
@login_required
def calendarView():
  months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep', 'Oct', 'Nov', 'Dec']
  month = None
  events = getAllEvents(session.get("email"))
  if request.args.get('month'):
    themes = getThemes()
    response = None
    month = request.args.get('month')
    if month == months.index(month):
      next_month_index = months.index(month) + 1
      response = getMonth(months[months.index(next_month_index)])
    else:
      response = getMonth(months[months.index(month) - 1])
  else:
    themes = getThemes()
    month = datetime.now().month
  response = ''
  if months.index(month) == 12:
    month = months[months.index('Jan')]
  if month == months.index(month):
    response = getMonth(months[months.index(month)])
  else:
    response = getMonth(months[months.index(month)])
  return Response(render_template("components/full_cal/cal.html", themes=themes, response=response,json_events=events), status=200, mimetype='text/html')

@app.route("/api/addEvent", methods=["POST"])
@login_required
def addEvent():
  months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep', 'Oct', 'Nov', 'Dec']
  if request.method == 'POST':
    user = session.get("email")
    event = request.form.get('event_title')
    month = request.form.get('event_month')
    date = request.form.get('event_date')
    time = request.form.get('event_time')
    description = request.form.get('event_description')
    events = {}

    events["user"] = user
    events['event_title'] = event
    events['event_month'] = month
    events['event_date'] = date
    events['event_time'] = time
    events['event_description'] = description

    json_event = json.dumps(events)

    addOneEvent(events)

    events = getAllEvents(session.get("email"))
    
    month = months[datetime.now().month - 1]
    response = getMonth(months[months.index(month)])
    
    return Response(render_template("components/full_cal/cal.html", response=response,json_events=events), status=200, mimetype="text/html")
  else:
    return Response(status=404, mimetype="text/html")
    
"""@app.route("/api/GetEvent", methods=["GET"])
def getEvent():
  if request.method == 'GET':
    response = searchOneEvent(event)
    json_event = json.dumps(response)
    return Response(json_event, status=200, mimetype="application/json")"""

@app.route("/api/getAllEvents", methods=["GET"])
@login_required
def getEvents():
  if request.method == 'GET':
    events = getAllEvents()
    json_events = json.dumps(events)
    return Response(json_events, status=200, mimetype="text/html")

@app.route("/api/GetThemes", methods=["GET"])
@login_required
def apiThemes():
  if request.method == 'GET':
    themes = getThemes()
    json_themes = json.dumps(themes)
    return Response(json_themes, status=200, mimetype="application/json")


@app.route("/api/RemoveEvent", methods=["GET"])
@login_required
def removeEvent():
  if request.method == 'GET':
    event = request.args.get('event_title')
    response = deleteOneEvent(event)
    if not response:
      print("Error has occurred, please try again.")
    else:
      if response > 0:
        month = datetime.now().month
        response = getCalendar(month)
        events = getAllEvents()
        themes = getThemes()
        return Response(render_template("components/full_cal/cal.html", themes=themes, month=str(month), response=response, json_events=events), status=200, mimetype="text/html")
      else:
        message = "Event deletion failed. Please try again"
        return Response(render_template("pages/error.html", message=message), status=502, mimetype="text/html")