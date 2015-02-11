#! /usr/bin/env python
# -- encoding:utf - 8 --

import cPickle
import requests
import socket

from random import choice
from bs4 import BeautifulSoup

from constants.main import HEADERS
from log import logger


proxies_pickle = cPickle.load(open("best_daili", 'r'))
proxies_list = [{'http': 'http://%s' % (proxy)}
                for proxy in proxies_pickle]


class StatusException(Exception):
    def __init__(self, state):
        self.state = state

    def __str__(self):
        return repr(self.state)


def get_soup(xiami_url):
    proxies = choice(proxies_list)
    try:
        r = requests.get(xiami_url, headers=HEADERS, proxies=proxies,
                         timeout=6)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content)
            if not soup.title or soup.title.text == u'亲，访问受限了':
                raise StatusException('受限了')
        else:
            raise StatusException(r.status_code)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout,
            socket.timeout, StatusException) as e:
        logger.info('Proxy is %s error is %s' % (proxies, e))
        soup = get_soup(xiami_url)
        print('ConnectionError or timeout')
    return soup
