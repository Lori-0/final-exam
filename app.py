from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/assets/<path:path>')
def send_report(path):
    return send_from_directory('static/assets', path)