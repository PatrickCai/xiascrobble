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
