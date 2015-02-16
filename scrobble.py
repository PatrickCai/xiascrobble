import time

from controllers import user_contr
from lastxia import xia, last
from log import logger, x_conn_err
from utils import geventWorker
from utils.count import err_count


with open('constants/scrobble_workers', "r") as txt:
    SCROBBLE_WORKERS_NUMBER = int(txt.read())


def scrobble(one_user, progress):
    "@todo (use decorator to print progress)"
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
        # Log user
        user_info = "The total user is %s ||| " % (len(all_users))
        duration_info = "The duration is %s " % (time.time() - start_time)
        logger.info(user_info + duration_info)
        # Log connection error
        xiami_err_count = err_count.report_count()
        x_err_count_info = 'The xiami connection error number is %s,\
            total user %s' % (xiami_err_count.count, len(all_users))
        x_err_percentage = 'The percentage is %s' %\
            (int(float(xiami_err_count.count) / float(all_users) * 100))
        x_conn_err.info(x_err_count_info + x_err_percentage)
        time.sleep(60)
