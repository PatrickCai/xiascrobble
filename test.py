from controllers import last_contr
from models import user
from constants.main import BASE_DIR
from utils.log import color

session_key = 'a5238b292a474bef7dfd2c868dadf726'


if __name__ == "__main__":
    print(color(BASE_DIR))
    # user.random_user_times()
    # network = last_contr.get_network()
    # network.session_key = session_key
    # print(network.get_authenticated_user())
    # print(colorstr("Hello", "r"))
    # pass
