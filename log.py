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
visitlg = logging.getLogger("Visitor")
visitlg.setLevel(level)

visitFilename = 'visitor.log'
vfh = logging.FileHandler(visitFilename)
vfh.setLevel(level)
vfh.setFormatter(form)
visitlg.addHandler(vfh)
