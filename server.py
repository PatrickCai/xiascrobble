from tornado.ioloop import IOLoop
from application import application

from log import visitlg

PORT = "8888"


if __name__ == "__main__":
    visitlg.info("***************************************************")
    application.listen(PORT, xheaders=True)
    IOLoop.current().start()
