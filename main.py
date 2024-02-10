from flask import Flask, render_template, request, redirect, url_for, flash, session, stream_template, Response, request_finished, g
from flask_session import Session
from flask_caching import Cache
from apscheduler.schedulers.background import BackgroundScheduler
from cs50 import SQL
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from helper import login_required
from operator import itemgetter
import time
from blueprints.login import login_bp
from blueprints.feed import feed_bp, newPost
from blueprints.upload import upload_bp
from blueprints.notifications import notify_bp

from functools import wraps

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(feed_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(notify_bp)

app.secret_key = 'Here is the key!@#$%^&*()'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_THRESHOLD'] = 10
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'mp4'}

app.config.from_mapping(config)
cache = Cache(app)

Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memories.db")

@app.route("/")
@login_required
def index():
  if request.method == "GET":
    post_request = db.execute("SELECT * FROM posts")
    return render_template( "auth/pages/board.html", title = post_request )
  else:
    pass

@app.route('/board', methods=['GET'])
@login_required
def board():
  if request.method == "GET":
      post_request = db.execute("SELECT * FROM posts")
      return render_template( 'auth/pages/board.html', title = post_request )
  else:
    return "<h1> Method not allowed</h1>"

@app.route('/reactions')
@login_required
def react():
  if request.method == "POST":
    post_id = request.form.get("post_id")
    likes = request.form.get("like")
    loves = request.form.get("love")
    
    if likes:
      db.execute("UPDATE posts SET post_like = post_like + 1 WHERE post_id = ?", post_id)
      app.logger.info('POST request to add likes to %s', post_id)
      return render_template('auth/pages/board.html')
    elif loves:
      db.execute("UPDATE posts SET post_love = post_love + 1 WHERE post_id = ?", post_id)
      app.logger.info('POST request to add love to %s', post_id)
      return render_template('auth/pages/board.html')
    else:
      return render_template('auth/pages/board.html')
  else:
    return "<h1> Method not allowed</h1>"

@app.route('/users')
@login_required
def users():
  if request.method == "GET":
    users = db.execute("SELECT * FROM users")
    return render_template('auth/ui/user_list.html', users = users)
  else:
    return render_template('auth/pages/board.html')

@app.route('/profile')
@login_required
def profile():
  if request.method == "GET":
    return render_template('auth/pages/profile.html')
  else:
    return "<h1>Error: request method not allowed!</h1>"

@app.route('/notifications')
@login_required
def notifications():
  if request.method == "GET":
    
    id = session.get("user_id")
    
    notifications = db.execute("SELECT * FROM posts")
    print(str(notifications))
    
    user_info = db.execute("SELECT * FROM users WHERE user_id = ?", id)
    print(str(user_info))
    
    if notifications:
      for notification in notifications:
        return """
              <div class="divide-y divide-gray-100 dark:divide-gray-700">
        <a href="#" class="flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700">
          <div class="flex-shrink-0">
            <div class="absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-blue-600 border border-white rounded-full dark:border-gray-800">
              <svg class="w-2 h-2 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 18">
                <path d="M1 18h16a1 1 0 0 0 1-1v-6h-4.439a.99.99 0 0 0-.908.6 3.978 3.978 0 0 1-7.306 0 .99.99 0 0 0-.908-.6H0v6a1 1 0 0 0 1 1Z"/>
                <path d="M4.439 9a2.99 2.99 0 0 1 2.742 1.8 1.977 1.977 0 0 0 3.638 0A2.99 2.99 0 0 1 13.561 9H17.8L15.977.783A1 1 0 0 0 15 0H3a1 1 0 0 0-.977.783L.2 9h4.239Z"/>
              </svg>
            </div>
          </div>
          <div class="w-full ps-3">
            <div class="text-gray-500 text-sm mb-1.5 dark:text-gray-400">New message from <span class="font-semibold text-gray-900 dark:text-white">{user_info[0]['user_username']}</span>: {notification['post_content']}</div>
            <div class="text-xs text-blue-600 dark:text-blue-500">a few moments ago</div>
          </div>
        </a>
      </div>
      """
    else:
      return """
          <div class="divide-y divide-gray-100 dark:divide-gray-700">
        <a href="#" class="flex px-4 py-3 hover:bg-gray-100 dark:hover:bg-gray-700">
          <div class="flex-shrink-0">
            <div class="absolute flex items-center justify-center w-5 h-5 ms-6 -mt-5 bg-blue-600 border border-white rounded-full dark:border-gray-800">
              <svg class="w-2 h-2 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 18">
                <path d="M1 18h16a1 1 0 0 0 1-1v-6h-4.439a.99.99 0 0 0-.908.6 3.978 3.978 0 0 1-7.306 0 .99.99 0 0 0-.908-.6H0v6a1 1 0 0 0 1 1Z"/>
                <path d="M4.439 9a2.99 2.99 0 0 1 2.742 1.8 1.977 1.977 0 0 0 3.638 0A2.99 2.99 0 0 1 13.561 9H17.8L15.977.783A1 1 0 0 0 15 0H3a1 1 0 0 0-.977.783L.2 9h4.239Z"/>
              </svg>
            </div>
          </div>
          <div class="w-full ps-3">
            <div class="text-gray-500 text-sm mb-1.5 dark:text-gray-400">New message from <span class="font-semibold text-gray-900 dark:text-white">{user_info[0]['user_username']}</span>: notification['post_content']</div>
            <div class="text-xs text-blue-600 dark:text-blue-500">a few moments ago</div>
          </div>
        </a>
      </div>
      """
  else:
    return """
    <div class="flex flew-col justify-center items-center text-lg">
    <h1><span><strong>Error:</strong></span> request method not allowed!</h1>
    </div>
    """

@app.route('/logout')
def logout():
  session.clear()
  return render_template( 'un_auth/pages/login.html' )

@app.route('/register', methods=['GET', 'POST'])
def register():
  error = None

  if request.method == 'POST':
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")

    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    hash = generate_password_hash(password)
    conf_password = request.form.get("conf-password")
    bio = request.form.get("biography")
    city = request.form.get("city")
    state = request.form.get("state")
    country = request.form.get("country")
    dateAcctCreated = dt_string

    if password != conf_password:
      error = 'Passwords do not match'
      return render_template('un_auth/pages/register.html', error=error)
    elif len(email) < 0:
      error = 'Email is required'
      return render_template('un_auth/pages/register.html', error=error)
    elif len(bio) < 0:
      error = 'Bio is required'
      return render_template('un_auth/pages/register.html', error=error)
    elif len(city) < 0:
      error = 'City is required'
      return render_template('un_auth/pages/register.html', error=error)
    elif len(state) < 0:
      error = 'State is required'
      return render_template('un_auth/pages/register.html', error=error)
    elif len(country) < 0:
      error = 'Country is required'
      return render_template('un_auth/pages/register.html', error=error)
    else:
      session["username"] = username
      db.execute(
          "INSERT INTO users (user_email, user_username, user_password, user_bio, user_city, user_state, user_country, user_created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
          email, username, hash, bio, city, state, country, dateAcctCreated)
      message = 'Account created successfully!'
      return render_template('un_auth/pages/login.html', message=message)

  else:
    return render_template('un_auth/pages/register.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8081, debug=True)
