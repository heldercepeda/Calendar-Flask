from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np


def list_for_calendar(month=None, year=None):
    today = datetime.strftime(datetime.now(), '%Y-%m-%d')
    first_of_month = f'{year}-{month}-01'
    table_dates = pd.DataFrame(index=[i for i in range(6)], columns=[i for i in range(7)])
    first = pd.to_datetime(first_of_month) - relativedelta(days=pd.to_datetime(first_of_month).dayofweek)
    for i in range(table_dates.shape[0]):
        for j in range(table_dates.shape[1]):
            table_dates.iloc[i, j] = first + relativedelta(days=i * 7 + j)
    final_list = []
    for i in range(table_dates.shape[0]):
        week_list = []
        for j in range(table_dates.shape[1]):
            day_list = []
            day_list.append(table_dates.iloc[i, j].strftime("%d"))  # day of month (two digits)
            day_list.append(table_dates.iloc[i, j].strftime("%B"))  # month (full name)
            day_list.append(table_dates.iloc[i, j].strftime("%Y"))  # year (four digits)
            day_list.append(table_dates.iloc[i, j].strftime("%A"))  # day of week (full name)
            day_list.append(datetime.strftime(table_dates.iloc[i, j], '%Y-%B-%d'))  # full day
            week_list.append(day_list)
        final_list.append(week_list)
    next_nonth = pd.to_datetime(first_of_month) + relativedelta(months=1)
    prev_nonth = pd.to_datetime(first_of_month) - relativedelta(months=1)
    return final_list, next_nonth.strftime("%B"), next_nonth.strftime("%Y"),\
           prev_nonth.strftime("%B"), prev_nonth.strftime("%Y")