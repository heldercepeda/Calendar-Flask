from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np


def list_for_calendar(month=None, year=None):
    today = datetime.strftime(datetime.now(), '%Y-%m-%d')
    if not month:
        month = pd.to_datetime(today).strftime("%B")
    if not year:
        year = pd.to_datetime(today).strftime("%Y")
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
            day_list.append(table_dates.iloc[i, j].strftime("%d"))
            day_list.append(table_dates.iloc[i, j].strftime("%B"))
            week_list.append(day_list)
        final_list.append(week_list)
    next_nonth = pd.to_datetime(first_of_month) + relativedelta(months=1)
    prev_nonth = pd.to_datetime(first_of_month) - relativedelta(months=1)
    return final_list, next_nonth.strftime("%B"), next_nonth.strftime("%Y"),\
           prev_nonth.strftime("%B"), prev_nonth.strftime("%Y")