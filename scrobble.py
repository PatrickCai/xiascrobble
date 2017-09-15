import time

from controllers import user_contr
from lastxia import xia, last
from constants.main import SCROBBLE_WORKERS_NUMBER
from utils.log import logger, x_conn_err, color
from utils import geventWorker

from utils.logControl import log_user

def scrobble(one_user, progress):
    "@todo (use decorator to print progress)"
    (titles, artists, track_times, record_time) = xia.xiami(one_user)
    # logger.info([titles, artists, track_times, record_time])
    if titles:
        last.scrobble(one_user, titles, artists, track_times, record_time)
    print(progress)


if __name__ == "__main__":
    gevent_worker = geventWorker.Worker(SCROBBLE_WORKERS_NUMBER)
    while 1:
        start_time = time.time()
        all_users = user_contr.get_available_users()

        #Gevent Boss/Worker
        boss = gevent_worker.generate_boss(all_users)
        workers = gevent_worker.generate_workers(scrobble)
        gevent_worker.joinall(workers, boss)

        #Log
        log_user(all_users, start_time)
        log_connection_err(all_users)
        time.sleep(60)
