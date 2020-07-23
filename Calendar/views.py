from datetime import datetime
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from Calendar import app, db, bcrypt
from Calendar.functions.generic import list_for_calendar
from Calendar.static.models import User
from Calendar.static.forms import RegistrationForm, LoginForm



@app.route('/', methods=["GET","POST"])
@app.route('/home', methods=["GET","POST"])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('calendar'))
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=False)
            return redirect(url_for('calendar'))
        else:
            return redirect(url_for('home'))
    return render_template(
        'login.html',
        title="login",
        form=form
    )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('calendar'))
    form = RegistrationForm()
    if form.validate_on_submit() and request.method == "POST":
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template(
            'register.html',
            title="register",
            form=form
        )



@app.route('/calendar')
@login_required
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
