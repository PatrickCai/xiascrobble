from tornado.ioloop import IOLoop
from application import application

from log import logger

PORT = "8888"


if __name__ == "__main__":
    logger.info("***************************************************")
    application.listen(PORT)
    IOLoop.current().start()
