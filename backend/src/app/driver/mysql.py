#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mysql.py
@Time    :   2019/12/30 11:29:52
@Version :   1.0
@Desc    :   mysql 进行操作
'''
import uuid
import pymysql
from ..driver.base import Table

class MysqlTable(Table):

    def __init__(self, db, **kwargs):
        self._cursor = 
        sql = """
        CREATE TABLE IF NOT EXISTS `runoob_tbl`(
        `runoob_id` INT UNSIGNED AUTO_INCREMENT,
        `runoob_title` VARCHAR(100) NOT NULL,
        `runoob_author` VARCHAR(40) NOT NULL,
        `submission_date` DATE,
        PRIMARY KEY ( `runoob_id` )
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """


    def insert_one(self, _id=None, **kwargs):
    """ Insert a single document.
    Args:
        _id(optional): Host where the database server is located.
        port(optional): MySQL port to use, default is usually OK. (default: 3306)
    Raise:
        ConnectionFailure: Raised when a connection to the database cannot be made or is lost.
    """
    if _id is not None:
        _id = uuid.uuid4()

class MysqlCore(object):

    def __init__(self, host='localhost', user="root", password="root", database=None, port=3306, **kwargs):
        """
        Args:
            host(optional): Host where the database server is located.
            port(optional): MySQL port to use, default is usually OK. (default: 3306)
        Raise:
            ConnectionFailure: Raised when a connection to the database cannot be made or is lost.
        """
        self._db = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=database,
                                    port=port,
                                    **kwargs)
          