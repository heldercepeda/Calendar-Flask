from datetime import datetime
from flask import render_template
from Calendar import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'login.html'
    )


@app.route('/register')
def register():
    return render_template(
        'register.html'
    )


@app.route('/calendar')
def calendar():
    return render_template(
        'calendar.html',
        day = datetime.today().strftime("%d"),
        month = datetime.today().strftime("%B"),
        year = datetime.today().strftime("%Y")
    )
