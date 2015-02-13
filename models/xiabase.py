from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


with open("constants/mysqlpassword.secret", "r") as txt:
    mysql_passwd = txt.read()


def get_session():
    engine = create_engine(
        "mysql://root:%s@localhost/xiascrobble?charset=utf8" % (mysql_passwd),
        echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session
