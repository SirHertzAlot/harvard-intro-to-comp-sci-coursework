from functools import wraps
from flask import g, flash, render_template, request, session

def login_required(f):
  @wraps(f)
  def decorated_func(*args, **kwargs):
    if 'username' not in session:
      return render_template('un_auth/pages/login.html')
    return f(*args, **kwargs)
  return decorated_func