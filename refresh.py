import time

from controllers import user_contr
from utils.zeus import read_constants_file


def update_user_times():
    user_contr.update_user_times()


if __name__ == "__main__":
    while 1:
        sleep_minutes = int(read_constants_file('refreshTime'))
        print("Now you can stop me")
        time.sleep(sleep_minutes * 60)
        update_user_times()
