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
