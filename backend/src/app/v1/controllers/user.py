#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2020/01/02 15:01:23
@Version :   1.0
@Desc    :   None
'''
import logging
from enum import Enum
from typing import List, Dict
from defaultlist import defaultlist

from app.check.data import (
    check_value, 
    check_type, 
    typeassert_func_dict, 
    typeassert_func_list
)
from app.v1.serializers.user import SerializerUser

class BaseCreateUser(Enum):

    INPUT_TYPE =  {'name': str, 'remark': str, 'password': str, 'role': str}
    OUTPUT_TYPE = {'name': str, 'remark': str, 'role': str, 
                    'user_id': int, 'reset': bool, 'id': str, 
                    'created_time': int}
    OUTPUT_KEYS = list(OUTPUT_TYPE.keys())


def base_create_user(_input: Dict) -> Dict:
    """base function, create a new user.
    Args:
        _input: the dict class.
        Example:

            _input = {
                'name': 'test', 
                'remark': 'test', 
                'password': 'test', 
                'role': "admin
            }
    Returns:
        The model of user.
    """
    check_type(_input, BaseCreateUser.INPUT_TYPE.value)
    _object = SerializerUser.create_user(**_input)
    _output = _object.todict(BaseCreateUser.OUTPUT_KEYS.value)
    check_type(_output, BaseCreateUser.OUTPUT_TYPE.value)
    return _object


class CreateUser(Enum):

    INPUT_TYPE =  {'name': str, 'remark': str, 'password': str, 'role': str}
    OUTPUT_TYPE = {'name': str, 'remark': str, 'role': str, 
                    'user_id': int, 'reset': bool, 'id': str, 
                    'created_time': int}
    OUTPUT_KEYS = list(OUTPUT_TYPE.keys())


@typeassert_func_dict(_type=CreateUser.INPUT_TYPE.value)
def create_user(_input: Dict) -> Dict:
    """ Create a user
    """
    _object = base_create_user(_input) # call base function
    _output = _object.todict(CreateUser.OUTPUT_KEYS.value)
    output = {
        "name": "123",
        "remark": "123",
        "role": "admin",
        "id": "123",
        "user_id": 123,
        "reset": False, 
        "created_time": 123
    }
    check_type(_output, CreateUser.OUTPUT_TYPE.value)
    return _output


@typeassert_func_list(_type=CreateUser.INPUT_TYPE.value)
def create_users(_input: List) -> List:
    """ Create multiple users
    """
    _output = defaultlist(dict)
    for _index, add_user in enumerate(_input):
        _output[_index] = create_user(add_user)
    return _output




# def check_userinfo(_input: dict, _check_keys:list) -> list:
#     """
#     _input = { "name": "admin","password": "21232f297a57a5a743894a0e4a801fc3"}
#     _check_keys = ["name", "password"]
#     """
#     pass
#     # model_user = model_user_tool.get_by_name(name=_input.get("name"))
#     # isTrue, keys = check_value(_input, _demo: dict, _keys: list)