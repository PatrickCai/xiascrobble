import os

import tornado.web

# from utils.log import logger
from urls import urls
from utils.zeus import read_constants_file


cookie_secret = read_constants_file("cookie_secret.secret")

SETTINGS = {
    'debug': True,
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'cookie_secret': cookie_secret,
    'login_url': '/first?',
}


application = tornado.web.Application(
    handlers=urls,
    **SETTINGS)
