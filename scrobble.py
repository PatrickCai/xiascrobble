import time

from controllers import user_contr
from lastxia import xia, last
from constants.main import SCROBBLE_WORKERS_NUMBER
from utils.log import logger, x_conn_err, color
from utils import geventWorker
from utils.count import err_count


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

        boss = gevent_worker.generate_boss(all_users)
        workers = gevent_worker.generate_workers(scrobble)
        gevent_worker.joinall(workers, boss)

        # Log user
        user_info = "The user number is %s ||| " % (color(len(all_users)))
        duration_info = "Running time is  %s sec" %\
            (color(int(time.time() - start_time)))
        logger.info(user_info + duration_info)

        # Log connection error
        xiami_err_count = err_count.report_count()
        x_err_count_info = 'The xiami connection error number is %s,\
total user %s .' % (color(xiami_err_count), color(len(all_users)))
        x_err_percentage = 'The percentage is %s' %\
            (color(int(float(xiami_err_count) / float(len(all_users)) * 100)))
        x_conn_err.info(x_err_count_info + x_err_percentage)
        time.sleep(60)
