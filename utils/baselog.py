import logging
import os


from constants.main import BASE_DIR


format = '%(asctime)s %(message)s'
datefmt = "%Y/%m/%d %H:%M:%S"
level = logging.DEBUG
form = logging.Formatter(fmt=format, datefmt=datefmt)


class Xslog(logging.getLoggerClass()):
    def __init__(self, info, filename):
        super(Xslog, self).__init__(info)
        self.setLevel(level)
        file_path = os.path.join(BASE_DIR, 'logs/%s' % (filename))
        vfh = logging.FileHandler(file_path)
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
