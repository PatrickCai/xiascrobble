from tornado.ioloop import IOLoop
from application import application

from utils.log import visitlog
from utils.zeus import read_constants_file

PORT = int(read_constants_file('port.sercet'))


if __name__ == "__main__":
    visitlog.info("***************************************************")
    application.listen(PORT, xheaders=True)
    IOLoop.current().start()
