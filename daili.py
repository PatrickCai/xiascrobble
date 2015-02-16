#! /usr/bin/env python
# -- encoding:utf - 8 --

import time
import cPickle
import requests
import random

from constants.main import HEADERS
from bs4 import BeautifulSoup
from utils import geventWorker
from log import proxylog

with open("constants/ip_proxy_times") as txt:
    ip_proxy_times = int(txt.read())


def try_proxy(daili, progress, good_dailis):
    proxies = {'http': 'http://%s' % (daili)}
    try:
        req = requests.get('http://www.xiami.com/space/feed/u/793/type/9',
                           proxies=proxies, timeout=2,
                           headers=HEADERS)

        if req.status_code == 200:
            soup = BeautifulSoup(req.content)
            is_foreign_ip = soup.find('input', id='J_email')
            if not soup.title.text == u'亲，访问受限了' and not is_foreign_ip:
                good_dailis.append(daili)
                print('%s' % (proxies))
        else:
            print('fail%s' % (req.status_code))
    except (requests.exceptions.ConnectionError,
            requests.exceptions.Timeout):
        print('fail')
    print(progress)


def get_daili():
    workers_number = 15
    good_dailis = []
    dailis = cPickle.load(open('constants/original_ips', 'r'))
    # Only try 300 one time
    random.shuffle(dailis)
    dailis = dailis[0: 300]
    gevent_worker = geventWorker.Worker(workers_number)
    boss = gevent_worker.generate_boss(dailis)
    workers = gevent_worker.generate_workers(try_proxy, good_dailis)
    gevent_worker.joinall(boss, workers)

    random.shuffle(good_dailis)
    proxylog.info("Update %s proxy ips" % len(good_dailis))
    cPickle.dump(good_dailis, open('constants/good_ips', 'w'))
    print("Daili get %s " % len(good_dailis))

if __name__ == "__main__":
    get_daili()
    proxylog.info("Update over")
