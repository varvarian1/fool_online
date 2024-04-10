from flask import render_template
from app import app

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/registration")
def registration():
    return render_template('registration.html')