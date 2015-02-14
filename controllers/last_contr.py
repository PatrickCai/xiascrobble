from utils import pylast
from constants.main import API_KEY, API_SECRET
from constants.error import INVALID_SESSION, NOT_USER
from log import logger
from models import user


def get_network():
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
    return network


def get_lastfm_url():
    '''
    Fetch the url in the last.fm to make user connect to the last.fm
    '''
    network = get_network()
    sg = pylast.SessionKeyGenerator(network)
    callback_url = 'http://scrobble.chom.me/third'
    url = sg.get_web_auth_url(callback_url)
    return url


def token_to_session(access_token):
    '''
    Convert user's access_token into session in last.fm
    '''
    network = get_network()
    sg = pylast.SessionKeyGenerator(network)
    session_key = sg.get_web_auth_session_key(access_token)
    return session_key


def scrobble(network, artist, title, timestamp):
    try:
        network.scrobble(artist, title, timestamp)
    except pylast.WSError as e:
        if (str(e) == INVALID_SESSION or str(e) == NOT_USER):
            user.set_invalid(network.session_key)
            logger.info("The reason %s the sessio key %s "
                        % (e, network.session_key))
        logger.info(network.session_key)


def scrobble_many(network, tracks):
    '''
    Scrobble many tracks
    '''
    try:
        network.scrobble_many(tracks)
    except pylast.WSError as e:
        if (str(e) == INVALID_SESSION or str(e) == NOT_USER):
            user.set_invalid(network.session_key)
            logger.info("The reason %s the sessio key %s "
                        % (e, network.session_key))
        logger.info("Network error %s " % network.session_key)


def update_now_playing(network, artist, title):
    '''
    Update now playing
    @todo(Refactor it with decorators)
    '''
    try:
        network.update_now_playing(artist, title)
    except pylast.WSError as e:
        if (str(e) == INVALID_SESSION or str(e) == NOT_USER):
            user.set_invalid(network.session_key)
            logger.info("The reason %s the sessio key %s "
                        % (e, network.session_key))
        logger.info(network.session_key)


def rm_scrobble(network, artist, title, timestamp):
    try:
        user = network.get_authenticated_user()
        library = pylast.Library(user, network)
        library.remove_scrobble(artist, title, timestamp)
    except Exception as e:
        logger.info(e)
        logger.info(network.session_key)
