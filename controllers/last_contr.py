from utils import pylast
from constants.main import API_KEY, API_SECRET
from log import logger


def get_network():
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
    return network


def get_lastfm_url(user_xiami_id):
    '''
    Fetch the url in the last.fm to make user connect to the last.fm
    '''
    network = get_network()
    sg = pylast.SessionKeyGenerator(network)
    # @todo(change it to the real ip)
    callback_url = 'http://127.0.0.1:81/third?username=%s'\
        % (user_xiami_id)
    url = sg.get_web_auth_url(callback_url)
    return url


def token_to_session(access_token):
    '''
    Convert user's access_token into session in last.fm
    '''
    network = get_network()
    sg = pylast.SessionKeyGenerator(network)
    logger.info("The token is %s" % (access_token))
    session_key = sg.get_web_auth_session_key(access_token)
    return session_key
