from datetime import datetime
from flask import render_template, request, redirect
from flask_login import login_user, logout_user, current_user, login_required

from Calendar import app
from Calendar.functions.generic import list_for_calendar
from Calendar.static.models import User
from Calendar.static.forms import RegistrationForm, LoginForm



@app.route('/')
@app.route('/home', methods=["GET","POST"])
def home():
    form = LoginForm()
    return render_template(
        'login.html',
        title="login",
        form=form
    )


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template(
        'register.html',
        title="register",
        form=form
    )



@app.route('/calendar')
def calendar():
    month = request.args.get('month')
    year = request.args.get('year')
    if not month:
        month = datetime.today().strftime("%B")
    if not year:
        year = datetime.today().strftime("%Y")
    final_list, next_month, next_month_year, prev_month, prev_month_year = list_for_calendar(month,year)
    return render_template(
        'calendar.html',
        final_list=final_list,
        next_month=next_month,
        next_month_year=next_month_year,
        prev_month=prev_month,
        prev_month_year=prev_month_year,
        actual_year = year,
        actual_month = month,
        today = datetime.today().strftime('%Y-%B-%d'),
        title="calendar"
    )
