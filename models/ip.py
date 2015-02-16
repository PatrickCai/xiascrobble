from utils.xsredis import r_cli

good_ips_name = 'good_ips:list'


def store_ips(good_ips):
    '''
    Store all good ips to redis
    '''
    r_cli.sadd(good_ips_name, *good_ips)


def get_random_ip():
    '''
    Pick one ip by random
    '''
    proxies_ip = r_cli.srandmember(good_ips_name)
    return proxies_ip


def delete_ip(proxies_ip):
    '''
    Delete the specific proxies ip
    '''
    r_cli.srem(good_ips_name, proxies_ip)


def get_ip_number():
    ip_number = r_cli.scard(good_ips_name)
    ip_number = int(ip_number)
    return ip_number
