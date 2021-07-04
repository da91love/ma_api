from datetime import datetime


def is_date(DateAsStr):
    try:
        datetime.strptime(DateAsStr, '%Y-%m-%d')
        return True

    except Exception as e:
        return False