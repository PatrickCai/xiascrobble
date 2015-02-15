import os

import tornado.web

# from log import logger
from urls import urls

with open("constants/cookie_secret.secret", "r") as secret:
    cookie_secret = secret.read()

SETTINGS = {
    'debug': True,
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'cookie_secret': cookie_secret,
    'login_url': '/first?',
}


application = tornado.web.Application(
    handlers=urls,
    **SETTINGS)
