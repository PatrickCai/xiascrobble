import random

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from xiabase import get_session
from log import logger, visitlg
from constants.main import MAX_TIMES

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    '@todo change the users_id to user_id'
    users_id = Column(Integer, primary_key=True)
    session = Column(String(length=45))
    record_time = Column(String(length=45))
    times = Column(Integer())
    register_time = Column(String(length=45))
    last_loved_song = Column(String(length=45))
    is_valid = Column(Integer(), default=1)


def verify_user(xiami_user_id):
    '''
    Verify whether user has already registered the xiascrobble
    @todo(Fix the issue when the user has already register but cancel
        the lastfm session)
    '''
    db_session = get_session()
    user = db_session.query(User)\
        .filter(User.users_id == xiami_user_id).first()
    return bool(user)


def insert_user(user_xiami_id, session, record_time, now_time):
    '''
    Insert the user into database
    '''
    db_session = get_session()
    times = 0
    last_loved_song = "None"
    visitlg.info("Register sucessfully user id is %s" % user_xiami_id)
    user = User(users_id=user_xiami_id, session=session,
                record_time=record_time, times=times,
                last_loved_song=last_loved_song, register_time=now_time)
    db_session.add(user)
    db_session.commit()


def get_available_users():
    '''
    Return all users whose 1.times is zero 2.the valid user
    These users' listening history will be scrobbled
    '''
    db_session = get_session()
    available_users = db_session.query(User)\
        .filter(User.times == 0).filter(User.is_valid == 1).all()
    return available_users


def not_listening(user_id):
    '''
    When the user is not listening change its time to MAX
    '''
    db_session = get_session()
    one_user = db_session.query(User)\
        .filter(User.users_id == user_id).first()
    one_user.times = MAX_TIMES
    db_session.commit()


def update_record_times(user_id, record_time):
    '''
    When a user has scrobbled,it should update its last record_time
    to the latest time
    '''
    db_session = get_session()
    one_user = db_session.query(User)\
        .filter(User.users_id == user_id).first()
    one_user.record_time = record_time
    db_session.commit()


def update_user_times():
    '''
    Update all users whose times is larger than 0
    and minus 1
    '''
    db_session = get_session()
    all_users = db_session.query(User)\
        .filter(User.times > 0).filter(User.is_valid == 1).all()
    for all_user in all_users:
        all_user.times -= 1
    db_session.commit()


def random_user_times():
    '''
    Initialize the users' times to random
    '''
    random_times = [0, 1, 2, 3, 4, 5]
    db_session = get_session()
    all_users = db_session.query(User).all()
    for all_user in all_users:
        all_user.times = random.choice(random_times)
    db_session.commit()


def get_one_user():
    '''
    Get one user as test user
    '''
    db_session = get_session()
    user = db_session.query(User)\
        .filter(User.users_id == 168488).first()
    return user


def set_invalid(session_key):
    db_session = get_session()
    user = db_session.query(User)\
        .filter(User.session == session_key).first()
    user.is_valid = 0
    db_session.commit()


def get_all_users():
    db_session = get_session()
    users = db_session.query(User).all()
    return users
