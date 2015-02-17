from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.zeus import read_constants_file

Base = declarative_base()

mysql_passwd = read_constants_file('mysqlpassword.secret')


def get_session():
    engine = create_engine(
        "mysql://root:%s@localhost/xiascrobble?charset=utf8" % (mysql_passwd),
        echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session
