from flask import Flask, Blueprint, request, jsonify, render_template, session
from flask_session import Session
from blinker import signal
from cs50 import SQL
from datetime import datetime
from helper import login_required

feed_bp = Blueprint('feed', __name__, template_folder='templates')

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///memories.db")

newPost = signal('newPost')

@feed_bp.route('/getfeed', methods=["GET"])
@login_required
def getfeed():
  if request.method == "GET":
    feed_cache = ""
    
    print("GET request received for /Getfeed")
    feed_request = db.execute("SELECT * FROM posts")
    owner = db.execute("SELECT * FROM users WHERE user_id = ?", feed_request[0]['post_owner_id'])
    
    for i in range(len(feed_request)):
      feed_request = db.execute("SELECT * FROM posts")
      post_reactions = feed_request[i]['post_reactions']
      post_content = feed_request[i]['post_content']
      post_title = feed_request[i]['post_title']
      feed_cache = feed_cache + f'''
      <div class="bg-white rounded-lg shadow-md p-6">
        <div class="flex items-center justify-between">
          <h2 class="text-xl font-bold">{post_title}</h2>
          <span class="text-gray-500">February 6, 2024</span>
        </div>
      <p class="mt-4">{post_content}</p>
        <div class="flex justify-end mt-4">
        <a href="#" class="text-blue-500 hover:text-blue-700">Read more</a>
        </div>
      </div>
      '''
      return render_template('auth/ui/feed.html', title = feed_cache, ownerObj = owner)
  return 
 

@feed_bp.route('/postfeed', methods=["POST", "GET"])
@login_required
def postfeed():
  if request.method == "POST":
    rows = db.execute("SELECT * FROM users WHERE user_username = ?", session.get("username"))
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")

    title = request.form.get("title")
    content = request.form.get("post")

    user_id = session.get("user_id")
    
    if 'file' in request.files:
      f = request.files['file']
      f.save(secure_filename(f.filename))
      message = flash("File successfully uploaded")
    else: 
      post = db.execute("INSERT INTO posts (post_title, post_content, post_created_at, post_owner_id) VALUES (?, ?, ?, ?)", title, content, dt_string, user_id)

      message = "Post successful"
  
      print("Emitting Signal!!!")
      
      result = newPost.send(post)
      print(f'Result print: {result} result type: {type(result)}')
      
      if 'None' not in result:
        print(f'Signal received by {result}')
      
      post_request = db.execute("SELECT * FROM posts")
      return render_template('auth/pages/board.html', title = post_request, message = message)
  else:
    post_request = db.execute("SELECT * FROM posts ORDER BY post_created_at DESC")
    return render_template('auth/pages/board.html', title = post_request)
    