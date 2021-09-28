"""
This is a basic flask application
"""

import time

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Return the main page with a timestamp"""
    time_str = time.strftime("%b %d %Y %H:%M:%S", time.gmtime())
    return f"<h1>Hello world</h1><br><h3>{time_str}</h3>"
