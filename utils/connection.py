#! /usr/bin/env python
# -- encoding:utf - 8 --

import cPickle
import requests
import socket

from random import choice
from bs4 import BeautifulSoup

from constants.main import HEADERS
from utils.count import err_count
from log import logger


proxies_pickle = cPickle.load(open("constants/good_ips", 'r'))
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
            is_foreign_ip = soup.find('input', id='J_email')
            if not soup.title or soup.title.text == u'亲，访问受限了'\
                    or is_foreign_ip:
                raise StatusException('受限了')
        else:
            raise StatusException(r.status_code)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout,
            socket.timeout, StatusException, socket.error):
        soup = get_soup(xiami_url)
        err_count.add()
        print('ConnectionError or timeout')
    return soup
