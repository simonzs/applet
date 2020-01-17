#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
@Time    :   2020/01/02 14:39:47
@Version :   1.0
@Desc    :   router
'''

from app.v1.handlers import base, user

url_patterns = [
    (r"/", base.BaseHandler),
    (r"/api/v1", base.BaseHandler),

    # User Management
    (r"/api/v1/login", user.LoginHandler),
    (r"/api/v1/user", user.UserHandler),
]