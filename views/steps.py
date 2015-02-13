import tornado.web
import tornado.httpclient

from log import visitlg
from controllers import user_contr, last_contr


class WelcomeHandler(tornado.web.RequestHandler):
    def get(self):
        visitlg.info("In the welcome")
        self.render("index.html")


class FirstHandler(tornado.web.RequestHandler):
    def get(self):
        visitlg.info("In the first html")
        self.render("first.html")


class VerifyHandler(tornado.web.RequestHandler):
    '''
    Verify whether the user is already in the database
    '''
    def get(self):
        user_xiami_id = self.get_argument("username")
        do_exist = user_contr.verify_user(user_xiami_id)
        if not do_exist:
            '@todo(Consider the situation the register process is stopped)'
            self.set_secure_cookie("user_xiami_id", user_xiami_id,
                                   expires_days=1)
        self.write({"do_exist": str(do_exist)})


class SecondHandler(tornado.web.RequestHandler):
    '''
    Get the xiami user id and make user to connect to the last.fm
    '''
    def get(self):
        '@todo(Consider the user click the url for mistake, redirect it to\
               the welcome page)'
        user_xiami_id = int(self.get_secure_cookie("user_xiami_id"))
        visitlg.info("In the second html, the user id is %s" % (user_xiami_id))
        lastfm_url = last_contr.get_lastfm_url()
        self.render("second.html", lastfm_url=lastfm_url)


class ThirdHandler(tornado.web.RequestHandler):
    '''
    save user's  lastfm session
    '''
    def get(self):
        user_xiami_id = int(self.get_secure_cookie("user_xiami_id"))
        visitlg.info("In the third html user id is %s " % (user_xiami_id))
        access_token = self.get_argument("token")
        session = last_contr.token_to_session(access_token)
        user_contr.save_session(user_xiami_id, session)
        self.clear_cookie("user_xiami_id")
        self.render("third.html")


class TestHandler(tornado.web.RequestHandler):
    '''
    For test purpose ,the url is /test
    '''
    def get(self):
        pass
