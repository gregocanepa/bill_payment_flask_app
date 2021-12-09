from datetime import datetime


def string_to_datetime(string_date):
    return datetime.strptime(string_date, "%Y-%m-%d")
