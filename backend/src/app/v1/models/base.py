# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2019/12/03 20:13:36
@Author  :   Simon 
@Version :   1.0
@Desc    :   None
'''


import uuid
from copy import deepcopy
from abc import abstractmethod, ABCMeta
from app.utils.decorator import check_type

class Interface(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *args, **kwargs): pass

    @abstractmethod
    def _type(self): pass


class DataObject(Interface):

    def __init__(self, _input):
        self._data = deepcopy(_input)
        check_type(self._data, self._type)

    @property
    def id(self):
        return self._data['_id']
        
    @property
    def created_time(self):
        return self._data['created_time']

    @property
    def updated_time(self):
        return self._data['updated_time']