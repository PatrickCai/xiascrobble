from controllers import last_contr
from models import user

session_key = 'a5238b292a474bef7dfd2c868dadf726'


if __name__ == "__main__":
    # user.random_user_times()
    network = last_contr.get_network()
    network.session_key = session_key
    print(network.get_authenticated_user())
