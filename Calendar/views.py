from datetime import datetime
from flask import render_template
from Calendar import app

@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'login.html'
    )


@app.route('/register')
def register():
    """Renders the home page."""
    return render_template(
        'register.html'
    )


@app.route('/calendar')
def calendar():
    """Renders the home page."""
    return render_template(
        'calendar.html'
    )
