from flask import render_template
from app import app

@app.route('/')
def Home():
    return render_template("index.html")


