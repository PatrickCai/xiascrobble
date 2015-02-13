import time

from controllers import user_contr


def update_user_times():
    user_contr.update_user_times()

with open("constants/refreshTime", "r") as txt:
    sleep_minutes = int(txt.read())

if __name__ == "__main__":
    while 1:
        print("Now you can stop me")
        time.sleep(sleep_minutes * 60)
        update_user_times()
