from controllers import last_contr
from models import user

session_key = '46cbf306e994b82bcb03c361b91f13b8'


if __name__ == "__main__":
    # user.random_user_times()
    network = last_contr.get_network()
    network.session_key = session_key
    print(network.get_authenticated_user())
