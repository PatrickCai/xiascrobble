from tornado.ioloop import IOLoop
from application import application

from log import visitlg

import cPickle


with open("constants/port.secret") as txt:
    PORT = txt.read()


if __name__ == "__main__":
    visitlg.info("***************************************************")
    application.listen(PORT, xheaders=True)
    IOLoop.current().start()
