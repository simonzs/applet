#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/01/15 18:04:15
@Version :   1.0
@Desc    :   适配器

'''
import logging
from enum import IntEnum
from app.adapter.base import _DATABASE, _PORT, _TIMEOUT, _HOST
from app.adapter.database import Database
from app.adapter.table import Table


conf = {
    "databases": {
        "backend": {
            "type": _DATABASE.MONGODB,
            "host": _HOST.MONGODB,
            "port": _PORT.MONGODB,
            "timeout": _TIMEOUT.MONGODB
        },
        "statsite": {
            "type": _DATABASE.INFLUXDB,
            "host": _HOST.INFLUXDB,
            "port": _PORT.INFLUXDB,
            "timeout": _TIMEOUT.INFLUXDB
        },
        "telegraf": {
            "type": _DATABASE.INFLUXDB,
            "host": _HOST.INFLUXDB,
            "port": _PORT.INFLUXDB,
            "timeout": _TIMEOUT.INFLUXDB
        }
    },
    "tables": {
        "users": "backend"
    }
}


db_conf = conf['databases']
table_conf = conf['tables']


class Adapter(object):

    @classmethod
    def get_database(cls, 
                name: str,
                host: str='localhost', 
                port:_PORT=_PORT.MONGODB, 
                _type:_DATABASE=_DATABASE.MONGODB, 
                timeout:_TIMEOUT=_TIMEOUT.MONGODB, 
                **kwargs) -> Database:
        return  Database(host, port, _type, timeout, **kwargs)

    @classmethod
    def get_table(cls,
                name: str,
                _database: Database,
                **kwargs) -> Table:
        return Table(name, _database)


for db_name, _conf in db_conf.items():
    locals()['db_{}'.format(db_name)] = Adapter.get_database(
                                                name=db_name,
                                                host=_conf['host'],
                                                port=_conf['port'],
                                                _type=_conf['type'],
                                                timeout=_conf['timeout']
                                                )


for table_name, _db_name in table_conf.items():
    locals()['table_{}'.format(table_name)] = Adapter.get_table(
                                                name=table_name,
                                                _database=locals()['db_{}'.format(_db_name)]
                                                )