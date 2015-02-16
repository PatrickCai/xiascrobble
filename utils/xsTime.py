import time
from datetime import datetime, timedelta


def transform_minutes(last_time):
    last_time = datetime.strptime(last_time, '%Y-%m-%d %H:%M:%S')
    minutes = (datetime.now() - last_time).seconds / 60
    return minutes


def get_last_minutes(minutes):
    '''
    Get the time before minutes from now on
    '''
    record_time = datetime.now() - timedelta(minutes=minutes)
    record_time = record_time.strftime('%Y-%m-%d %H:%M:%S')
    return record_time


def sleep(seconds, msg=None):
    '''
    Similar to time.sleep() ,add the additional msg
    '''
    if not msg:
        print("Now you should wait %s seconds" % (seconds))
    else:
        print("Now you should wait %s" % (msg))
    time.sleep(seconds)


def is_clock(func, *args, **kwargs):
    '''
    If it is like 17:00 or 13:00, it will run the function
    '''
    if datetime.now().minute == 0:
        return func(*args, **kwargs)
