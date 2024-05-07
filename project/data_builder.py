from tinydb import TinyDB, Query
import datetime, json
import calendar

db = TinyDB("calendar.json")
event = Query()

def getNow():
  return datetime.datetime.now()

def getCurrentMonth():
  return getNow().month

def genMonths():
  months = [] 
  for x in range(1,13):
   months.append(calendar.month_abbr[x])
  return months

def genHours():
  hours = {}
  for x in range(1,24):
    if x > 12:
      hour = x - 12
      hours[f"hour {x}"] = hour
      hours[f"meridian {x}"] = "PM"
    else:
      hours[f"hour {x}"] = str(x)
      hours[f"meridian {x}"] = " AM"
  return hours

def genDays():
  current_time = getNow()
  months = genMonths()
  
  calObj = {}

  year = current_time.year
  current_month = current_time.month

  month_cal_obj = calendar.TextCalendar(firstweekday=6)

  for i in range(1, 13):
    month = {}
    month_cal_str = month_cal_obj.formatmonth(year, i).split('\n')
    month['nameofmonth'] = months[i - 1]
    month['yearofmonth'] = year
    month['dayofweek'] = month_cal_str[1].split('\n')
    month['week1'] = month_cal_str[2].split('\n')
    month['week2'] = month_cal_str[3].split('\n')
    month['week3'] = month_cal_str[4].split('\n')
    month['week4'] = month_cal_str[5].split('\n')
    month['week5'] = month_cal_str[6].split('\n')
    calObj[f'{i}'] = month
  
  return calObj

def buildDB(calendar):
  months_table = db.table('months')
  if months_table.insert(calendar) < 1:
    print("Insertion to DB has failed.")
  else:
    print("Successfully inserted calendar into database.")

def addThemes():
  themes = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'gray', 'black']
  themes_table = db.table('themes')
  for i in range(len(themes)):
    string = {}
    string['theme_name'] = themes[i].upper()
    string['theme_value'] = themes[i]
    if themes_table.insert(string) < 1:
      print("Insertion to DB has failed.")
    else:
      print("Successfully inserted themes into database.")

def addHours():
  hours_table = db.table('hours')
  hours = genHours()
  if hours_table.insert(hours) < 1:
    print("Insertion to DB has failed.")
  else:
    print("Successfully inserted hours into database.")


addHours()