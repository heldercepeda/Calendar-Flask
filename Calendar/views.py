from datetime import datetime
from flask import render_template
from Calendar import app
from Calendar.functions.generic import list_for_calendar

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
    final_list, next_month, next_month_year, prev_month, prev_month_year = list_for_calendar(month="December", year="2020")
    print(final_list)
    return render_template(
        'calendar.html',
        final_list=final_list,
        next_month=next_month,
        next_month_year=next_month_year,
        prev_month=prev_month,
        prev_month_year=prev_month_year
    )
