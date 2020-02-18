#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   table.py
@Time    :   2020/01/15 10:28:56
@Version :   1.0
@Desc    :   表进行操作, 
    https://api.mongodb.com/python/current/examples/aggregation.html
    https://docs.mongodb.com/manual/core/map-reduce/
'''
import logging
from uuid import uuid4
from typing import Dict
from abc import abstractmethod, ABC
from app.adapter.base import _DATABASE
from app.adapter.result import InsertOneResult


# 表中数据的操作
# class interface(metaclss=ABCMeta):
class interface(ABC):
    
    @abstractmethod
    def __init__(self, *args, **kwargs): pass
    
    @abstractmethod
    def bulk_write(self, *args, **kwargs): pass

    # insert -> insert_one
    @abstractmethod
    def insert_one(self, *args, **kwargs): pass

    # insert -> insert_many
    @abstractmethod
    def insert_many(self, *args, **kwargs): pass

    # update -> replace
    @abstractmethod
    def replace_one(self, *args, **kwargs): pass

    # update -> update_one
    @abstractmethod
    def update_one(self, *args, **kwargs): pass

    # update -> update_many
    @abstractmethod
    def update_many(self, *args, **kwargs): pass

    # update -> find_one_and_replace
    @abstractmethod
    def find_one_and_replace(self, *args, **kwargs): pass

    # update -> find_one_and_update
    @abstractmethod
    def find_one_and_update(self, *args, **kwargs): pass

    # find -> aggregate 
    @abstractmethod
    def aggregate(self, *args, **kwargs): pass

    # find -> aggregate_raw_batches 
    @abstractmethod
    def aggregate_raw_batches(self, *args, **kwargs): pass

    # find -> watch
    @abstractmethod
    def watch(self, *args, **kwargs): pass

    # find -> find
    @abstractmethod
    def find(self, *args, **kwargs): pass

    # find -> find_raw_batches
    @abstractmethod
    def find_raw_batches(self, *args, **kwargs): pass

    # find -> find_one
    @abstractmethod
    def find_one(self, *args, **kwargs): pass

    # delete -> find_one_and_delete
    @abstractmethod
    def find_one_and_delete(self, *args, **kwargs): pass

    # delete -> delete_one
    @abstractmethod
    def delete_one(self, *args, **kwargs): pass

    # delete -> delete_many
    @abstractmethod
    def delete_many(self, *args, **kwargs): pass

    # count -> count_documents
    @abstractmethod
    def count_documents(self, *args, **kwargs): pass

    # count -> distinct
    @abstractmethod
    def distinct(self, *args, **kwargs): pass
    """Get a list of distinct values for key among all documents in this collection.
    """
    # index -> create_index
    @abstractmethod
    def create_index(self, *args, **kwargs): pass
    """Creates an index on this collection.
    """

    # index -> create_indexes
    @abstractmethod
    def create_indexes(self, *args, **kwargs): pass
    """Create one or more indexes on this collection.
    """

    # index -> drop_index
    @abstractmethod
    def drop_index(self, *args, **kwargs): pass
    """Drops the specified index on this collection.
    """

    # index -> drop_indexes
    @abstractmethod
    def drop_indexes(self, *args, **kwargs): pass
    """Drops all indexes on this collection.
    """

    # index -> reindex
    @abstractmethod
    def reindex(self, *args, **kwargs): pass
    """Rebuilds all indexes on this collection.
    """

    # index -> list_indexes
    @abstractmethod
    def list_indexes(self, *args, **kwargs): pass
    """Get a cursor over the index documents for this collection.
    """

    # index -> index_information
    @abstractmethod
    def index_information(self, *args, **kwargs): pass
    """Get information on this collection’s indexes.
    """

    # drop -> drop
    @abstractmethod
    def drop(self, *args, **kwargs): pass
    """Drop a collection.
    """

    # rename -> rename
    @abstractmethod
    def rename(self, *args, **kwargs): pass
    """Rename this collection.
    """

    # map_reduce -> map_reduce
    @abstractmethod
    def map_reduce(self, *args, **kwargs): pass
    """Perform a map/reduce operation on this collection.
    """

    # map_reduce -> inline_map_reduce
    @abstractmethod
    def map_reduce(self, *args, **kwargs): pass
    """Perform an inline map/reduce operation on this collection.
    """


class Table(interface):

    def __init__(self, name: str, _db) -> None: 
        self._name = name
        self._db = _db
        self._type = _db.type
        
    @property
    def table(self):
        if not hasattr(self, '_table'):
            self._table = self._db.get_table(self._name)
        return self._table

    def bulk_write(self, *args, **kwargs): pass

    def insert_one(self, document: Dict, _id: str=None, **kwargs): 
        if _id is None:
            _id = str(uuid4())
        insert_id, acknowledged, _data = self.table.insert_one(document, _id, **kwargs)
        return InsertOneResult(insert_id, acknowledged, _data)

    def insert_many(self, *args, **kwargs): pass

    def replace_one(self, *args, **kwargs): pass

    def update_one(self, *args, **kwargs): pass

    def update_many(self, *args, **kwargs): pass

    def find_one_and_replace(self, *args, **kwargs): pass

    def find_one_and_update(self, *args, **kwargs): pass

    def aggregate(self, *args, **kwargs): pass

    def aggregate_raw_batches(self, *args, **kwargs): pass

    def watch(self, *args, **kwargs): pass

    def find(self, *args, **kwargs): pass

    def find_raw_batches(self, *args, **kwargs): pass

    def find_one(self, *args, **kwargs): pass

    def find_one_and_delete(self, *args, **kwargs): pass

    def delete_one(self, *args, **kwargs): pass

    def delete_many(self, *args, **kwargs): pass

    def count_documents(self, *args, **kwargs): pass

    def distinct(self, *args, **kwargs): pass
    
    def create_index(self, *args, **kwargs): pass
    
    def create_indexes(self, *args, **kwargs): pass
    
    def drop_index(self, *args, **kwargs): pass
    
    def drop_indexes(self, *args, **kwargs): pass
    
    def reindex(self, *args, **kwargs): pass
    
    def list_indexes(self, *args, **kwargs): pass
    
    def index_information(self, *args, **kwargs): pass
    
    def drop(self, *args, **kwargs): pass
    
    def rename(self, *args, **kwargs): pass
    
    def map_reduce(self, *args, **kwargs): pass
    
    def map_reduce(self, *args, **kwargs): pass
