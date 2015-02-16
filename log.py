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


class Xslog(logging.getLoggerClass()):
    def __init__(self, info, filename):
        super(Xslog, self).__init__(info)
        self.setLevel(level)
        vfh = logging.FileHandler(filename)
        vfh.setLevel(level)
        vfh.setFormatter(form)
        self.addHandler(vfh)

    def info(self, message, request=None):
        if request:
            remote_ip = request.request.remote_ip
            headers = request.request.headers
            print(headers)
            super(Xslog, self).info("The ip is %s . %s"
                                    % (remote_ip, message))
        else:
            super(Xslog, self).info(message)


# for web visitors
visitlg = Xslog("visitor log", 'visitor.log')
# for logging sync loved songs
lovelog = Xslog("love", "logs/love.log")
# for recording updating proxy ips
proxylog = Xslog("proxy", "logs/proxy.log")
# For recording xiami connnectio error
x_conn_err = Xslog("Xiami connectio error", "logs/x_conn_err.log")
