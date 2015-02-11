import gevent

from lastxia import xia, last
from models import user
from log import logger


if __name__ == "__main__":
    test_user = user.get_one_user()
    (titles, artists, track_times, record_time) = xia.xiami(test_user)
    logger.info((titles, artists, track_times, record_time))
    last.scrobble(test_user, titles, artists, track_times, record_time)
