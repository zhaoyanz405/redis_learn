#! /usr/bin/python
"""
分布式锁

设：
资源res占用标记为1
"""
import os
import time
from multiprocessing import Process
from random import randint

from redis import StrictRedis

redis = StrictRedis(host='127.0.0.1')


def acquire(res='default') -> bool:
    """
    申请锁
    :param res: 资源名
    :return:
    """
    _pid = os.getpid()

    if redis.setnx(res, 1):
        redis.expire(res, 10)
        print('process(pid: %s) has acquired.' % _pid)
        return True
    return False


def release(res='default'):
    """
    释放锁
    :param res: 资源名
    :return:
    """
    _pid = os.getpid()
    print('process(pid: %s) will release.' % _pid)
    redis.delete(res)


def do_something(res):
    """
    对资源res做一些事情
    :param res:
    :return:
    """
    _pid = os.getpid()

    _retry = 0
    while _retry < 3:
        if acquire(res):
            print('process(pid: %s) is doing with %s' % (_pid, res))
            time.sleep(randint(1, 5))
            release(res)
            break
        else:
            time.sleep(2)
            print('process(pid: %s) is waiting. retry in 2s.' % _pid)


if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = Process(target=do_something, args=('lock',))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    print('----- end -----')
