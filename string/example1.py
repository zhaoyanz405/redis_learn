#! /usr/bin/python
"""
通过string存储结构化的数据
"""
import json

from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1')

user_info = {
    "name": "user1",
    "age": 18,
    "hometown": "Suzhou"
}

key = 'cache_user_info'
redis.set(key, json.dumps(user_info))
print(redis.get(key))
