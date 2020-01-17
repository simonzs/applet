#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   input.py
@Time    :   2020/01/02 14:45:37
@Version :   1.0
@Desc    :   the type of input
'''

# /api/v1/user/login

login_post = {
    "username": str,
    "password": str,
}

user_post = {
    "name": str,
    "remark": str,
    "password": str,
    "role": str,
}