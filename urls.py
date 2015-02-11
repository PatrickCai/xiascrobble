from views.steps import WelcomeHandler, FirstHandler
from views.steps import VerifyHandler, TestHandler, SecondHandler
from views.steps import ThirdHandler

urls = [
    (r"/", WelcomeHandler),
    (r"/first", FirstHandler),
    (r"/verify", VerifyHandler),
    (r"/second", SecondHandler),
    (r"/third", ThirdHandler),
    (r"/test", TestHandler),
]
