#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2020/01/02 17:00:03
@Version :   1.0
@Desc    :   和models通信, 返回的都是models对象
'''
import logging
from enum import IntEnum
from app.v1.models.user import ModelUser
from app.adapter import table_users

# 约定
class Role(IntEnum):

    ADMIN = 1 # 超级管理员
    OBSERVER = 2 # 观察者
    OPERATOR = 3 # 操作员
    VISITOR = 4 # 访客


class SerializerUser():

    @classmethod
    def create_user(
        cls, 
        name: str, 
        remark: str,
        password: str,
        role: str
        ):
        """
        Args:
            name: required, the username of added.
            remak: optional, the remark of added, default is the name
                    of added.
            password: optional, the password of added, default is 123.
            role: optional, the role of added, default is 4.
        Returns:
            The model of user
        """
        _data = {
            "name": name,
            "remark": remark,
            "password": password,
            "role": role
        }

        add_data = {
            "user_id": 123,
            "reset": False
        }
        result = table_users.insert_one(_data=_data)
        data= result.data
        return ModelUser(data)

