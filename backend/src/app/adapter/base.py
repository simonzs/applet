#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2019/12/26 18:18:55
@Version :   1.0
@Desc    :   数据库适配器, 适配mongodb、 mysql、 influx, 创建工厂模型
'''

from enum import IntEnum, Enum
from abc import abstractmethod, ABCMeta

class _DATABASE(IntEnum):

    MYSQL = 1   # mysql 数据库
    MONGODB = 2 # mongodb 数据库
    SQLITE = 3  # sqlite 数据库
    INFLUXDB = 4

class _PORT(IntEnum):

    MONGODB = 27017
    INFLUXDB = 8086

class _TIMEOUT(IntEnum):

    MONGODB = 1
    INFLUXDB = 1
    
class _HOST(Enum):

    MONGODB = '172.17.0.1'
    INFLUXDB = '172.17.0.1'
