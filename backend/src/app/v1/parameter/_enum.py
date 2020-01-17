#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   _enum.py
@Time    :   2020/01/02 17:33:12
@Version :   1.0
@Desc    :   None
'''


from enum import Enum


class RRRole(Enum):
    """Specify possible role modes"""
    ADMIN = {"12": 12}
    OPERATOR = 1
    OBSERVER = 2
