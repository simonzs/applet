# -*- encoding: utf-8 -*-
'''
@File    :   casbin.py
@Time    :   2019/12/03 20:12:50
@Author  :   Simon 
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

import casbin as casbin_core

from app.v1.settings import settings


class AclCore():

    def __init__(self):
        self.e = casbin_core.Enforcer(
            settings["acl"]["auth_model"], settings["acl"]["policy"], enable_log=False)

    def enforce(self, sub, obj, act):
        return self.e.enforce(sub, obj, act)


casbin = AclCore()
