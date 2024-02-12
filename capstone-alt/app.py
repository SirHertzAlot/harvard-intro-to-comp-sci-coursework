from flask import Flask, session

#Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pages/index.html")
