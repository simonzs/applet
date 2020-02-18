#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mongo.py
@Time    :   2019/12/26 17:01:54
@Version :   1.0
@Desc    :   mongodb 表进行操作
'''

import copy
import logging
import pymongo
from typing import Dict
from pymongo.errors import ConnectionFailure
from ..driver.base import Table

class Database():
    pass




class MongoTable(Table):

    def __init__(self, name:str, db, **kwargs):
        self._name = name
        self._db = db
    
    @property
    def table(self):
        if not hasattr(self, '_table'):
            self._table = self._db.get_collection(self._name)
        return self._table

    def insert_one(self, document: Dict, _id: str, **kwargs):
        if 'id' in document:
            raise KeyError('Not need id, but given: {}.'.format(document))
        logging.error(_id)
        logging.error(document)
        self.table.insert_one()
        insert_id = 123
        acknowledged = True
        _data = {
            "name": "123",
            "remark": "123",
            "password": "123",
            "role": "123",

            "user_id": 123,
            "reset": False, 
            "id": "123",
            "created_time": 123,
            "updated_time": 123
        }
        return insert_id, acknowledged, _data 


class MongoDatabase(Database):

    def __init__(self, 
                name: str, 
                host: str, 
                port: int= 27017, 
                **kwargs):

        _client = pymongo.MongoClient(host, port, **kwargs)
        try:
            _client.admin.command('ismaster')
        except ConnectionFailure:
            logging.exception('Service not available')
        self._db = _client.get_database(name=name)
        # self._db.command({"setParameter":1, "internalQueryExecMaxBlockingSortBytes":335544320})

    def get_table(self, name, **kwargs):
        """
        Args: 
            name: the name of table.
        """
        return MongoTable(name, self._db, **kwargs)

    def close(self):
        pass
