
# -*- encoding: utf-8 -*-
'''
@File    :   userinfo.py
@Time    :   2019/12/03 20:13:52
@Author  :   Simon 
@Version :   1.0
@Desc    :   None
'''

import logging
from typing import Any
from collections import defaultdict
from app.v1.models.base import DataObject
from app.v1.parameter.models import _object


class ModelUser(DataObject):

    """
    必须和parameter._object.user的keys必须一致
    """
    
    @property
    def _type(self):
        return _object.user

    @property
    def name(self):
        return self._data['user_id']

    @property
    def remark(self):
        return self._data['remark']

    @property
    def reset(self):
        return self._data['reset']

    @property
    def password(self):
        return self._data['password']

    @property
    def user_id(self):
        return self._data['user_id']

    @property
    def role(self):
        return self._data['role']
    
    def todict(self, keys: list) -> Any:
        """ 只输出需要的字段
        Args:
            keys: the list class
        Returns:
            A model of user, the dict class
        Raises:
            KeyError: An error 
        """
        _output = dict()
        for k in keys:
            if k not in self._data:
                raise KeyError("Missing {} field in {}".format(k, keys))
            _output.setdefault(k, self._data.get(k))
        return _output

