import datetime as dt


def ts_to_date(target):
    try:
        return dt.datetime.utcfromtimestamp(int(target)).strftime("yyyy-mm-dd")

    except Exception as e:
        target