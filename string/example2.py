#! /usr/bin/python
"""
通过string存储对象数据
"""
import pickle

from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1')


class User:
    """
    test object
    """

    def __init__(self, name, age, hometown):
        self.name = name
        self.age = age
        self.hometown = hometown

    def __str__(self):
        return 'User: name = %s, age = %s, hometown = %s' % (self.name, self.age, self.hometown)


user1 = User('user1', 18, 'Suzhou')
key = 'cache_user_info_pickle'
redis.set(key, pickle.dumps(user1))

user_from_redis = redis.get(key)
print('user_from_redis', user_from_redis)
user_after_loads = pickle.loads(user_from_redis)
print('user_after_loads', user_after_loads)
