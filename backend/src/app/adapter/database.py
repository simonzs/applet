#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   database.py
@Time    :   2020/01/15 18:11:37
@Version :   1.0
@Desc    :   adapt database
'''
import logging
from abc import  abstractmethod, abstractproperty, ABC
from app.adapter.base import _DATABASE, _PORT, _TIMEOUT
from app.adapter.table import Table
from app.driver.mongo import MongoDatabase


class interface(ABC):
    
    @abstractmethod
    def __init__(self, *args, **kwargs): pass
        
    
    # close -> close
    @abstractmethod
    def close(self, *args, **kwargs): pass


class Database(interface):
    

    def __init__(self,
                name:str, 
                host: str='localhost', 
                port: _PORT=_PORT.MONGODB, 
                _type: _DATABASE=_DATABASE.MONGODB, 
                timeout: _TIMEOUT=_TIMEOUT.MONGODB, 
                **kwargs) -> None: 
        self._name = name
        self._host = host
        self._port = port
        self._type = _type
        self.kwargs = kwargs

    # 适配不同数据库
    @property
    def db(self) -> object:
        if not hasattr(self, '_db'):
            if self._type == _DATABASE.MONGODB:
                return MongoDatabase(
                                self._name,
                                self._host.value,
                                self._port.value,
                                **self.kwargs
                            )
        return self._db

    @property
    def type(self):
        return self._type

    def get_table(self, name: str, **kwargs):
        return self.db.get_table(name, **kwargs)

    def close(self):
        if self._type == _DATABASE.MONGODB:
            self._client.close()
