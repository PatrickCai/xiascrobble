import time

from controllers import last_contr, user_contr
from log import logger


def scrobble(user, titles, artists, track_times, record_time):
    network = last_contr.get_network()
    network.session_key = user.session
    # if the music is playing on
    if (time.time() - track_times[0]) < 180:
        last_contr.update_now_playing(network, artists[0], titles[0])
    tracks = (titles, artists, track_times)
    scrobble_tracks = []
    for title, artist, timestamp in zip(*tracks):
        scrobble_track = {}
        scrobble_track['artist'] = artist
        scrobble_track['title'] = title
        scrobble_track['timestamp'] = timestamp
        scrobble_tracks.append(scrobble_track)

    last_contr.scrobble_many(network, scrobble_tracks)
    user_contr.update_record_times(user.users_id, record_time)


def love(one_user, loved_songs):
    '''
    Scrobble the user's today loved songs to the Last fm
    '''
    network = last_contr.get_network()
    network.session_key = one_user.session
    for loved_song in loved_songs:
        last_contr.love_track(loved_song.artist, loved_song.title,
                              network)
