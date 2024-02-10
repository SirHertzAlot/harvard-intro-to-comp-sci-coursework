from flask import Flask, Blueprint, request, jsonify, render_template, session
from blueprints.feed import newPost
from cs50 import SQL

notify_bp = Blueprint('notify', __name__, template_folder='templates')

@newPost.connect
def update_feed_subscriber(sender, **extra):
  db = SQL("sqlite:///memories.db")
  """
  This function is called by the signal to update the feed with new memories.
  """
  print(f"Received update_feed signal: {str(sender)} data: {str(extra)}")
  posts = db.execute("SELECT * FROM posts ORDER BY post_id DESC LIMIT 10")
  return render_template('auth/ui/feed.html', title = posts)

@newPost.connect
def update_notification_subscriber(sender, **extra):
  print(f"New post added to the database {str(extra)}")
  session['feed_cache'] = extra
  return update_notification_subscriber(sender, extra)