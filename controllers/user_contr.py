from models import user
from datetime import datetime, timedelta


def verify_user(user_xiami_id):
    '''
    Verify whether the user is already in the database
    There are two cases 1.the user is not in the database
    2. the user is invalid
    '''
    do_exist = user.verify_user(user_xiami_id)
    return do_exist


def save_session(user_xiami_id, session):
    '''
    Save user's last.fm session and register time
    '''
    record_time = datetime.now() - timedelta(minutes=20)
    record_time = record_time.strftime('%Y-%m-%d %H:%M:%S')
    now_time = datetime.now()
    user.insert_user(user_xiami_id, session, record_time, now_time)


def get_available_users():
    '''
    Return all users whose 1.times is zero 2.the valid user
    '''
    return user.get_available_users()


def update_record_times(user_id, record_time):
    '''
    When a user has scrobbled,it should update its last record_time
    to the latest time
    '''
    user.update_record_times(user_id, record_time)


def update_user_times():
    '''
    Update all users whose times is larger than 0
    and minus 1
    '''
    user.update_user_times()
