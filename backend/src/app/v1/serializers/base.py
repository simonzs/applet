#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2020/01/02 17:07:37
@Version :   1.0
@Desc    :   None
'''

from time import time
import math

from enum import IntEnum

from steamcontroller import \
    SCStatus, \
    SCButtons, \
    SCI_NULL

import steamcontroller.uinput as sui

from collections import deque

EXIT_PRESS_DURATION = 2.0

class Pos(IntEnum):
    """Specify witch pad or trig is used"""
    RIGHT = 0
    LEFT = 1