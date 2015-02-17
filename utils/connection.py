#! /usr/bin/env python
# -- encoding:utf - 8 --

import cPickle
import requests
import socket

from bs4 import BeautifulSoup

from constants.main import HEADERS
from utils.count import err_count
from utils.log import logger
from models.ip import get_random_ip, delete_ip


class StatusException(Exception):
    def __init__(self, state):
        self.state = state

    def __str__(self):
        return repr(self.state)


def get_soup(xiami_url):
    proxies_ip = get_random_ip()
    proxies = {'http': 'http://%s' % (proxies_ip)}
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
            socket.timeout, StatusException, socket.error) as e:
        delete_ip(proxies_ip)
        soup = get_soup(xiami_url)
        err_count.add_count()
        print(str(e))
    return soup
