#! /usr/bin/python
"""
hyperLoglog 100万条数据测试
"""
from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1')

for i in range(1000000):
    redis.pfadd('uv', 'user%d' % i)

    if i != 0 and i % 10000 == 0:
        count = redis.pfcount('uv')
        print(round((i - count) / count, 2))
