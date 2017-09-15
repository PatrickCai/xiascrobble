import time
from utils.count import err_count
from utils.log import logger, x_conn_err, color

def log_user(all_users, start_time):
    user_info = "The user number is %s ||| " % (color(len(all_users)))
    duration_info = "Running time is  %s sec" %\
        (color(int(time.time() - start_time)))
    logger.info(user_info + duration_info)


def log_connection_error(all_users):
        xiami_err_count = err_count.report_count()
        x_err_count_info = 'The xiami connection error number is %s,\
total user %s .' % (color(xiami_err_count), color(len(all_users)))
        x_err_percentage = 'The percentage is %s' %\
            (color(int(float(xiami_err_count) / float(len(all_users)) * 100)))
        x_conn_err.info(x_err_count_info + x_err_percentage)