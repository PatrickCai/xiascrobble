import time

import gevent

from controllers.last_contr import get_network
from log import logger
from utils import pylast


def scrobble(user, titles, artists, track_times, record_time):
    network = get_network()
    network.session_key = user.session
    # if the music is playing on
    is_play_on = False
    if (time.time() - track_times[0]) < 180:
        try:
            network.update_now_playing(artists[0], titles[0])
            is_play_on = True
        except pylast.WSError as e:
            logger(e)

    def scrobble(title, artist, timestamp):
        try:
            network.scrobble(artist, title, timestamp)
        except pylast.WSError as e:
            logger(e)

    def get_spawns():
        if is_play_on:
            tracks = (titles[1:], artists[1:], track_times[1:])
        else:
            tracks = (titles, artists, track_times)

        spawns = [gevent.spawn(scrobble, title, artist, timestamp)
                  for title, artist, timestamp
                  in zip(*tracks)]
        return spawns
    gevent.joinall(get_spawns())
