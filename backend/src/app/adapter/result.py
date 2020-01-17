#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   result.py
@Time    :   2020/01/16 18:21:06
@Version :   1.0
@Desc    :   None
'''
import logging
from typing import Dict

class Result():

    def __init__(self, _data: Dict, **kwargs) -> None:
        self._data = _data

    @property
    def data(self):
        return self._data


class InsertOneResult(Result):

    def __init__(self, insert_id: str, acknowledged: bool, _data: Dict, **kwargs):
        super().__init__(_data, **kwargs)
        self._insert_id = insert_id
        self._acknowledged = acknowledged
    
    @property
    def insert_id(self):
        return self._insert_id
    
    @property
    def acknowledged(self):
        return self._acknowledged