import requests
import json
from redis_db import connect_db
import random
#requests modul uses REST HTTP request get to load the quoets and JSON module with loads changes it from string to dictionary readable by Python
def get_quote():
    q_res = requests.get("https://dummyjson.com/quotes")
    loaded_q = json.loads(q_res.text)
    return loaded_q

def post_quote():
    r = connect_db()
    new_quotes = get_quote()
    for quote in new_quotes:
        r.push('new_quotes', quote)

def get_slump_quote():
    r = connect_db()
    new_quotes = r.lrange('new_quotes', 0, -1)
    return random.choice(new_quotes).decode('utf-8')




