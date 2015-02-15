from tornado.web import authenticated
from views.base import BaseHandler
from log import visitlg
from controllers import user_contr, last_contr


class WelcomeHandler(BaseHandler):
    def get(self):
        visitlg.info("In the welcome", self)
        self.render("index.html")


class FirstHandler(BaseHandler):
    def get(self):
        visitlg.info("In the first html")
        self.render("first.html")


class VerifyHandler(BaseHandler):
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


class SecondHandler(BaseHandler):
    '''
    Get the xiami user id and make user to connect to the last.fm
    '''
    @authenticated
    def get(self):
        '@todo(Consider the user click the url for mistake, redirect it to\
               the welcome page)'
        user_xiami_id = int(self.current_user)
        visitlg.info("In the second html, the user id is %s" % (user_xiami_id),
                     self)
        lastfm_url = last_contr.get_lastfm_url()
        self.render("second.html", lastfm_url=lastfm_url)


class ThirdHandler(BaseHandler):
    '''
    save user's  lastfm session
    '''
    @authenticated
    def get(self):
        user_xiami_id = int(self.current_user)
        visitlg.info("In the third html user id is %s " % (user_xiami_id),
                     self)
        access_token = self.get_argument("token")
        session = last_contr.token_to_session(access_token)
        user_contr.save_session(user_xiami_id, session)
        self.clear_cookie("user_xiami_id")
        self.render("third.html")


class TestHandler(BaseHandler):
    '''
    For test purpose ,the url is /test
    '''
    def get(self):
        pass
