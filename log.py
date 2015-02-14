import os
import logging

format = '%(asctime)s %(message)s'
datefmt = "%Y/%m/%d %H:%M:%S"
level = logging.DEBUG
filename = "xiascrobble.log"
filename = os.path.join(os.path.dirname(__file__), filename)

logger = logging.getLogger("XiaScrobble")
logger.setLevel(level)
form = logging.Formatter(fmt=format, datefmt=datefmt)

fh = logging.FileHandler(filename)
fh.setLevel(level)
fh.setFormatter(form)
logger.addHandler(fh)

# for people who visits the web


class Myvisitlg(logging.getLoggerClass()):
    def __init__(self, info):
        super(Myvisitlg, self).__init__(info)
        self.setLevel(level)
        visit_filename = 'visitor.log'

        vfh = logging.FileHandler(visit_filename)
        vfh.setLevel(level)
        vfh.setFormatter(form)
        self.addHandler(vfh)

    def info(self, message, request=None):
        if request:
            remote_ip = request.request.remote_ip
            headers = request.request.headers
            print(headers)
            super(Myvisitlg, self).info("The ip is %s . %s"
                                        % (remote_ip, message))
        else:
            super(Myvisitlg, self).info(message)


visitlg = Myvisitlg("visitor log")
