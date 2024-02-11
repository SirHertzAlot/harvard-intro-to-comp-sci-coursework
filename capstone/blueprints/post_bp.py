from flask import Blueprint, session
from cs50 import SQL

user_endpoint = Blueprint('user_endpoint', __name__,
                        template_folder='templates')

db = SQL("sqlite:///memories.db")

@user_endpoint.route('/api/post', methods=['POST'])
async def post():
    user_id = session['user_id']
    post = request.form.get(content)

    db.execute("INSERT INTO posts")
    return
