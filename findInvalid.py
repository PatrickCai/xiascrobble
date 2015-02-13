import gevent

from gevent.queue import Queue
from gevent import monkey
monkey.patch_socket()

from controllers import last_contr as lcont
from models import user
from log import logger

WORKERS_NUMBER = 10

tasks = Queue()


def user_scrobble(test_user):
    network = lcont.get_network()
    network.session_key = test_user.session

    test_track_artist = "Waxahatchee"
    test_track_title = "Catfish"
    test_track_timestamp = 1322612976

    lcont.scrobble(network, test_track_artist, test_track_title,
                   test_track_timestamp)
    lcont.rm_scrobble(network, test_track_artist, test_track_title,
                      test_track_timestamp)


def boss():
    all_users = user.get_all_users()
    for one_user in all_users:
        tasks.put_nowait(one_user)


def worker(worker_id):
    while not tasks.empty():
        task = tasks.get()
        user_scrobble(task)
        # logger.info("The worker %s has got task %s " % (worker_id, task))


def generate_workers():
    workers = [gevent.spawn(worker, worker_id)
               for worker_id in xrange(1, WORKERS_NUMBER + 1)]
    return workers


if __name__ == "__main__":
    test_user = user.get_one_user()
    user_scrobble(test_user)
    # gevent.spawn(boss).join()

    # workers = generate_workers()
    # gevent.joinall(workers)
