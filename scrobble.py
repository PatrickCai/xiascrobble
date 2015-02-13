import time

from controllers import user_contr
from lastxia import xia, last
from log import logger
from models import user
from utils import geventWorker

with open('constants/scrobble_workers', "r") as txt:
    SCROBBLE_WORKERS_NUMBER = int(txt.read())


def scrobble(one_user, progress):
    print(progress)
    (titles, artists, track_times, record_time) = xia.xiami(one_user)
    # logger.info([titles, artists, track_times, record_time])
    if titles:
        last.scrobble(one_user, titles, artists, track_times, record_time)


if __name__ == "__main__":
    gevent_worker = geventWorker.Worker(SCROBBLE_WORKERS_NUMBER)
    while 1:
        start_time = time.time()
        all_users = user_contr.get_available_users()

        boss = gevent_worker.generate_boss(all_users)

        workers = gevent_worker.generate_workers(scrobble)

        gevent_worker.joinall(workers, boss)
        logger.info("The total user is %s " % (len(all_users)))
        logger.info("The duration is %s " % (time.time() - start_time))
        print("Now you can stop it")
        time.sleep(60)
