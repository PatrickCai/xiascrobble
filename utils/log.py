from utils.baselog import Xslog


# For recording scrobbling basic information
logger = Xslog('xiascrobble log', "xiascrobble.log")

# for web visitors
visitlog = Xslog("visitor log", 'visitor.log')

# for logging sync loved songs
lovelog = Xslog("love", "love.log")

# for recording updating proxy ips
proxylog = Xslog("proxy", "proxy.log")

# For recording xiami connnection error
x_conn_err = Xslog("Xiami connectio error", "x_conn_err.log")


COLORS = {
    'ENDC': 0,
    'r': 31,
    'g': 32,
    'b': 36,
    'y': 33,
    'black': 30,
}


def color(mes, color='b'):
    inte = "\x1B[%d;%dm" % (1, COLORS[color])
    return "%s %s\x1B[0m" % (inte, mes)
