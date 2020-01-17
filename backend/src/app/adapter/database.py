#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   database.py
@Time    :   2020/01/15 18:11:37
@Version :   1.0
@Desc    :   adapt database
'''

from abc import  abstractmethod, abstractproperty, ABC
from app.adapter.base import _DATABASE, _PORT
from app.adapter.table import Table
from app.driver.mongo import MongoDatabase


class interface(ABC):
    
    @abstractmethod
    def __init__(self, *args, **kwargs): pass
        
    
    # close -> close
    @abstractmethod
    def close(self, *args, **kwargs): pass


class Database(interface):
    
    def __init__(self, _host: str, _port: _PORT, _type: _DATABASE, timeout: int, **kwargs) -> None: 
        self._host = _host
        self._port = _port
        self._type = _type
        self.kwargs = kwargs

    # 适配不同数据库
    @property
    def db(self) -> object:
        if hasattr(self, 'db'):
            return self._db
        elif self._type == _DATABASE.MONGODB:
            return MongoDatabase(
                                    self._host,
                                    self.port,
                                    **self.kwargs
                                )

    @property
    def type(self):
        return self._type
    
    def get_table(self, name: str, **kwargs):
        return self.db.get

    def close(self):
        if self._type == _DATABASE.MONGODB:
            self._client.close()
    


        