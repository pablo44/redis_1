import redis

#encapsulating connection in order to reuse it multiply as en instace "r"
def connect_db():
    r = redis.Redis(protocol= 3, host = '127.0.0.1', port = 6379, decode_responses= True)
    return r