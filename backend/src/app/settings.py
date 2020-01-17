# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2019/12/03 20:03:52
@Author  :   Simon 
@Version :   1.0
@Desc    :   
'''


import logging
import requests
import os.path
import json
import sys
import tornado.log

import tornado.options
from tornado.options import define, options
from app.v1.setttings import settings as v1_settings
from app.v2.setttings import settings as v2_settings


define("port", default=80, help="run on the given port", type=int)
__BASE_DIR__ = os.path.dirname(os.path.abspath(__file__))


settings = {
    "debug": True,
    "acl": {
        "auth_model": os.path.join(__BASE_DIR__, "conf/auth_model.conf"),
        "policy": os.path.join(__BASE_DIR__, "conf/policy.csv"),
    },
    "mongodb": {
        "addr": "mongodb://172.17.0.1:27017",
        "db": "applet"
    },
    "login_cookie": "app_cookie",
}


settings.update(v1_settings)


class APISettings():
    def __init__(self):
        global settings
        tornado.options.parse_command_line()


_settings = APISettings()
