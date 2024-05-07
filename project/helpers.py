from flask import url_for, session, redirect
from tinydb import TinyDB, Query
from datetime import datetime
import re, requests, json, calendar
from functools import wraps

# TinyDB

events_db = TinyDB("events.json")
cal_db = TinyDB("calendar.json")
users_db = TinyDB("users.json")
event = Query()

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
      if session.get("email") is None:
          return redirect("/login")
      return f(*args, **kwargs)
  return decorated_function

def getUser(userObj):
  accounts = users_db.table("accounts")
  
  user_account = accounts.search(event.email.matches(userObj["email"]))
  
  if user_account:
    return user_account[0]
  else:
    print("User not found")
    
def addUser(userObj):
  accounts = users_db.table("accounts")
  if accounts.insert(userObj) < 1:
    print("Insertion to DB has failed.")
  else:
    print("Insertion to DB was successful.")

def addOneEvent(json_events):
  table = events_db.table("events")
  if table.insert(json_events) < 1:
    print("Insertion to DB has failed.")
  else:
    print("Successfully inserted event into database.")

def searchOneEvent(event_date):
  response = events_db.search(event.event_date == event_date)[0]
  if response is None:
    print("Please try again.")
  else:
    print("Successfully retrieved one event document")
    return response

def getAllEvents(user):
  table = events_db.table('events')
  
  events = table.search(event.user.matches(user))
  if events is None:
    print("Query unsuccessful. Please try again.")
  else:
    print("Successfully retrieved all event documents")
    return events

def deleteOneEvent(eventToRemove):
  table = events_db.table('events')
  removedEvent = table.remove(event.event_title.any(eventToRemove))
  if not removedEvent:
    print("Please try again.")
  else:
    print("Successfully deleted event from database.")

def getMonth(month):
  months = cal_db.table('months')
  response = months.get(event.nameofmonth.matches(month))
  if response is None:
    print("Please try again.")
  else:
    print("Successfully retrieved month document")
    return response

def getDays():
  calObj = calendar.Calendar()
  month = datetime.now().month
  year = datetime.now().year
  if month is not None and year is not None:
    day = calObj.itermonthdays3(year, month)
    return day
  else:
    print("Error. Please try again.")
  
def getCalendar(month):
  months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep', 'Oct', 'Nov', 'Dec']
  response = ''
  for i in range(1,13):
    if month == i:
      response = getMonth(months[i - 1])
  if response is None:
    print("Please try again")
  else:
    print("Successfully retrieved calendar document")
    return response

def getHours():
  hours = cal_db.table('hours')
  response = hours.all()
  if response is None:
    print("Please try again.")
  else:
    print("Successfully retrieved hours document")
    return response

def getThemes():
  themes = cal_db.table('themes')
  response = themes.all()
  if response is None:
    print("Query unsuccessful, please try again.")
  else:
    print("Successfully retrieved themes document")
    return response

def getWeeks():
  weeks_db = TinyDB('weeks.json')
  weeks = weeks_db.table('weeks')
  response = weeks.all()
  if response is None:
    print("Query unsuccessful, please try again.")
  else:
    print("Query Successful, Successfully retrieved all weeks.")
    return response

def gotoWeek(month_str, current_date):
  response = getWeeks()
  for i in range(len(response[0])):
    for key, value in response[0].items():
      if key.__contains__(month_str.lower()):
        if value.__contains__(current_date):
          return value

# TODO: Finish function weeksView() so that it returns the current weeks in this month. Afterwards build JS function to iterate over results that are cached clientside to ensure user is able to cycle through weeks in the year.