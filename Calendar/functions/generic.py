from datetime import datetime


def get_calendar():
    day = datetime.today().strftime("%d")
    month = datetime.today().strftime("%B")
    year = datetime.today().strftime("%Y")
    print(day)
    print(month)
    print(year)
    return None