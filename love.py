from utils.geventWorker import Worker
from lastxia import last, xia
from controllers import user_contr
from utils.log import lovelog
from utils.zeus import read_constants_file
from models import user

WORKERS_NUMBER = int(read_constants_file("love_workers"))


def love(one_user, progress):
    loved_songs = xia.love(one_user)
    if loved_songs:
        last.love(one_user, loved_songs)
        last_loved_song_id = loved_songs[0].song_id
        user_id = one_user.users_id
        user_contr.update_last_loved(user_id,
                                     last_loved_song_id)
    print(progress)


if __name__ == "__main__":
    # one_user = user.get_one_user()
    # love(one_user, 1)
    lovelog.info("Start")
    gevent_worker = Worker(WORKERS_NUMBER)
    all_users = user_contr.get_all_love_users()
    boss = gevent_worker.generate_boss(all_users)
    worker = gevent_worker.generate_workers(love)
    gevent_worker.joinall(boss, worker)
    lovelog.info("Finish")
