#! /usr/bin/env python
# -- encoding:utf - 8 --

import re
import time
import collections

from datetime import datetime

from constants.main import XIAMI_USER_PREFIX
from constants.main import XIAMI_USER_LOVED_PREFIX
from constants.main import XIAMI_SONG_PREFIX

from utils.log import logger
from utils.connection import get_soup
from utils.xsTime import transform_minutes, get_last_minutes
from models import user as muser


Track = collections.namedtuple('Track',
                               ['song_id', 'title', "album", "artist"])


def xiami(user):
    '''
    Track_times : The tuple which contains the time which the
    track is listened by the user
    Record
    '''
    xiami_url = '%s%s' % (XIAMI_USER_PREFIX, user.users_id)
    soup = get_soup(xiami_url)
    last_time = user.record_time
    minutes = transform_minutes(last_time)
    # There are two situations (1') looking for the time label which is '分钟前'，
    # (2‘)looking for the time label which is '秒前|刚刚'
    track_times = soup.findAll('td', class_='track_time')
    track_times = [re.search(u'\d+', track_time.text).group()
                   for track_time in track_times
                   if re.search(u'分钟前', track_time.text)]
    second_html = soup.find('td', class_='track_time')

    second_exist = re.search(u'秒前|刚刚', second_html.text) \
        if second_html else False
    if track_times or second_exist:
        exists_times = [int(track_time) for track_time in track_times
                        if int(track_time) < 10]
        track_times = [int(track_time) for track_time in track_times
                       if int(track_time) < minutes]
        # !页面中存在刚刚收听的音乐时间小于十分钟则将times继续设为0
        record_time = None
        if track_times:
            record_time = get_last_minutes(minutes=track_times[0])
        track_times = [int(time.time() - track_time * 60)
                       for track_time in track_times]
        if second_exist:
            record_time = datetime.now()
            record_time = record_time.strftime('%Y-%m-%d %H:%M:%S')
            track_times.insert(0, int(time.time()))

        track_number = len(track_times)
        if record_time:
            track_htmls = soup.findAll('tr', id=re.compile('track_\d+'),
                                       limit=track_number)
            upper_htmls = [track_html.find('td', class_='song_name')
                           for track_html in track_htmls]
            artists_html = [artist_html.findAll('a')[1:]
                            for artist_html in upper_htmls]
            artists = []
            for artist in artists_html:
                all_artists = [one_artist.text for one_artist in artist
                               if not re.search('http://i.xiami.com',
                                                one_artist['href'])]
                all_artist = ' & '.join(all_artists)
                artists.append(all_artist)
            title_htmls = soup.findAll('a', href=re.compile('/song/\d+'),
                                       limit=track_number)
            titles = [title['title'] for title in title_htmls]
            return (titles, artists, track_times, record_time)
        elif exists_times:
            # User is still listening however last track has been scrobbled
            # database.modify_user(user[0], user[2])
            return [None] * 4
        else:
            muser.not_listening(user.users_id)
            # database.not_listening(user[0])
            return [None] * 4
    else:
        muser.not_listening(user.users_id)
        # database.not_listening(user[0])
        return [None] * 4


def love(one_user):
    user_id = one_user.users_id
    last_loved_song = one_user.last_loved_song
    xiami_url = '%s%s' % (XIAMI_USER_LOVED_PREFIX, user_id)
    soup = get_soup(xiami_url)
    songs_ids_htmls = soup.findAll('tr', id=re.compile('lib_song_\d+'))
    songs_ids = [re.search('lib_song_(\d+)', songs_IDs_html['id']).group(1)
                 for songs_IDs_html in songs_ids_htmls]
    if last_loved_song == 'None':
        loved_songs_ids = songs_ids
    elif last_loved_song in songs_ids:
        place = songs_ids.index(last_loved_song)
        loved_songs_ids = songs_ids[0: place]
    else:
        loved_songs_ids = songs_ids

    loved_songs = []
    for loved_song_ID in loved_songs_ids:
        love_url = '%s%s' % (XIAMI_SONG_PREFIX, loved_song_ID)
        soup = get_soup(love_url)
        title_html = soup.find("meta", {"property": 'og:title'})
        # @todo(See http://www.xiami.com/song/1771918283)
        if not title_html:
            continue
        title = title_html['content']
        album_artist_html = soup.find('table', id='albums_info')
        # There are some rare and special cases where the url doesn't fit
        # the normal one,so just ignore it.
        if not album_artist_html:
            continue
        album_html = album_artist_html.find('a',
                                            href=re.compile('/album/\d+'))
        album = album_html['title']
        artists_htmls = album_artist_html.findAll('tr')[1]
        '@todo(Fix the problem see \
        http://www.xiami.com/song/1772575223'
        artists_htmls = artists_htmls.findAll('a')
        artists = [artist_html.text for artist_html in artists_htmls
                   if artist_html.text != '']
        artist = ' & '.join(artists)
        track = Track(loved_song_ID, title, album, artist)
        loved_songs.append(track)
    return loved_songs
