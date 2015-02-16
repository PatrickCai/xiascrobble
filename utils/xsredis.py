import redis


r_cli = redis.StrictRedis(host="localhost", port=6379, db=0)
