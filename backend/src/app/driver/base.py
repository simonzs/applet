#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2019/12/30 09:55:42
@Version :   1.0
@Desc    :   数据库基础类, 创建工厂模型
'''

from abc import abstractmethod, ABCMeta


class Table(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *args, **kwargs): pass

    @abstractmethod
    def insert_one(self, *args, **kwargs): pass
    """
    Insert a single document.
    
    """


class Database(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *args, **kwargs): pass
    """ Client for Database instance
    """

    @abstractmethod
    def get_table(self, name): pass
    """
    Args:
        name: The name of the table
    Return:
    Raise:
    """






