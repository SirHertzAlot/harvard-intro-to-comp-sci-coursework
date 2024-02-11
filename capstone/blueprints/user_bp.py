from flask import Blueprint, session
from cs50 import SQL

user_endpoint = Blueprint('user_endpoint', __name__,
                        template_folder='templates')

db = SQL("sqlite:///memories.db")

@user_endpoint.route('/api/users/<user_id>')
async def show(user_id):
    user_id = session["user_id"]
    user_posts = await db.execute("SELECT * FROM posts WHERE user_id = ?", user_id)
    print(user_posts)
    for post in user_posts:
        """
            <div hx-get="/api/user/" hx-trigger="click" hx-target="#parent-div" hx-swap="outerHTML" class="col-lg-4">
                                <div class="card">
                                    <div class="card-body">
                                        <h4 class="card-title">Timeline</h4>
                                        <div class="timeline-">
                                            <ul class="timeline">
                                                <li>
                                                    <div class="timeline-badge primary"></div><a href="#" class="timeline-panel text-muted"><span>10 minutes ago</span><h6 class="m-t-5">Youtube, a video-sharing website, goes live.</h6></a>
                                                </li>
                                                <li>
                                                    <div class="timeline-badge warning"></div><a href="#" class="timeline-panel text-muted"><span>20 minutes ago</span><h6 class="m-t-5">Mashable, a news website and blog, goes live.</h6></a>
                                                </li>
                                                <li>
                                                    <div class="timeline-badge danger"></div><a href="#" class="timeline-panel text-muted"><span>30 minutes ago</span><h6 class="m-t-5">Google acquires Youtube.</h6></a>
                                                </li>
                                                <li>
                                                    <div class="timeline-badge success"></div><a href="#" class="timeline-panel text-muted"><span>15 minutes ago</span><h6 class="m-t-5">StumbleUpon is acquired by eBay.</h6></a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        """
    return
