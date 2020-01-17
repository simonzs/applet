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
from pymongo.errors import ConnectionFailure
from ..driver.base import Table

class Database():
    pass




class MongoTable(Table):

    def __init__(self, name:str, _db, **kwargs):
        pass


class MongoDatabase(Database):

    def __init__(self, name: str, _host='localhost', port= 27017, **kwargs):
        """
        Args:
            host(optional): hostname or IP address or Unix domain socket path of a single mongod
            or mongos instance to connect to, or a mongodb URI, or a list of hostnames / mongodb
            URIs.
            port(optional): port number on which to connect.
        Returns: 
            Client for a MongoDB instance, a replica set, or a set of mongoses.
        Raise:
            ConnectionFailure: Raised when a connection to the database cannot be made or is lost.
        """
        _client = pymongo.MongoClient(host, port, **kwargs)
        try:
            _client.admin.command('ismaster')
        except ConnectionFailure:
            logging.exception('Service not available')
        self._db = _client.get_database(name=name)
        self._db.command({"setParameter":1, "internalQueryExecMaxBlockingSortBytes":335544320})

    def get_table(self, name: str, _db, **kwargs):
        return MongoTable(name, self._db, **kwargs)

    def close(self):
        pass
