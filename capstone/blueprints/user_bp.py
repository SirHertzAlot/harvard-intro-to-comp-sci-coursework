from flask import Blueprint

user_endpoint = Blueprint('user_endpoint', __name__,
                        template_folder='templates')

@user_endpoint.route('/api/users/<user_id>')
def show(user_id):
    user_posts = db.execute("SELECT * FROM posts WHERE user_id = ?", user_id)
    print(user_posts)
    return """
    
"""
