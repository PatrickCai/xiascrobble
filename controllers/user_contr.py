from models import user
from datetime import datetime, timedelta


def verify_user(user_xiami_id):
    '''
    Verify whether the user is already in the database
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
