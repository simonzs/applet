#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   output.py
@Time    :   2020/01/02 14:52:09
@Version :   1.0
@Desc    :   None
'''

# /api/v1/user/login
login_post = {
    "id": str,
    "created_time": int,
    "name": str,
    "remark": str,
    "user_id": int,
    "reset": bool, 
    # "ticket": str, # 特有
}

user_post = {
    "id": str,
    "created_time": int,
    "reset": bool, 
    "user_id": int,

    "name": str,
    "remark": str,
    "role": str
}