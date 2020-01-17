#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   speed.py
@Time    :   2020/01/10 17:25:33
@Version :   1.0
@Desc    :   check speed
'''

"""
一个页面最多两个接口， 接口过多， 会影响速度
添加接口监控的部分:
    1. handlers.
    2. controllers.
    
"""




# 1. 上下文管理, 用于检测实际的接口速度
class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
    def __enter__(self):
        self.start = clock()
        return self
    def __exit__(self, *args):
        self.end = clock()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print('elapsed time: %f ms' % self.msecs)


import time
from timeit import Timer
from functools import partial

# 2. 用于检测， controller逻辑的速度
def _timeit_analyze_(func, params):
    t1 = Timer("%s()" % func.__name__, "from __main__ import %s" % func.__name__)
    # print "{:<20}{:10.6} s".format(func.__name__ + ":", t1.timeit(exec_times))
    print("{}{} s".format(func.__name__, t1.timeit(number=1)))

def funct(data):
    time.sleep(1)
    print(data)

_timeit_analyze_(funct, "123")