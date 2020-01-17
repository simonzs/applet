#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2020/01/02 14:40:45
@Version :   1.0
@Desc    :   None
'''
import logging
from typing import List, Dict
from app.check.data import typeassert, check_type
from app.v1.parameter.handlers import _input, _output
from app.v1.controllers import user as controller_user

from app.v1.handlers import base

class UserHandler(base.AsyncHandler):

    # @typeassert(check_type=_input.user_post)
    def do_post(self, data):
        """Add a new user or multiple users.

        Args:
            [
                {
                    "name": "test",
                    "remark": "remark",
                    "password": "password",
                    "role": "admin"
                }
            ]
            Or
            {
                "name": "test",
                "remark": "remark",
                "password": "password",
                "role": "admin"
            }
            
        Returns:
            [
                {
                    "created_time": 123,
                    "id": "123",
                    "name": "123",
                    "remark": "123",
                    "reset": false,
                    "user_id": 123
                }
            ]
            Or            
            {
                "created_time": 123, # 数据路自动添加的
                "id": "123", # 数据库自动添加的
                "reset": false, # 数据库自动添加的
                "user_id": 123, # 数据库自动添加的

                "name": "123",
                "remark": "123", 
                # password 不返回
                "role": "admin"
            }

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
            ValueError: An error 
        """
        if isinstance(data, List):
            [check_type(_create_user,  _input.user_post) for _create_user in data]
            result = controller_user.create_users(data)
            [check_type(_userinfo, _output.user_post) for _userinfo in result]
        if isinstance(data, Dict):
            check_type(data, _input.user_post)
            result = controller_user.create_user(data)
            check_type(result, _output.user_post)
        return self.success(result)

class LoginHandler(base.AsyncHandler):

    @typeassert(check_type=_input.login_post)
    def do_post(self, data):
        result = controller_user.check_userinfo(data)
        return self.success(result)


