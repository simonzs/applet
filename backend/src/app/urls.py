# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
@Time    :   2019/11/27 11:29:39
@Author  :   Simon 
@Version :   1.0
@Desc    :   None
'''

from app.v1.urls import url_patterns as v1_url_patterns


url_patterns = list()
url_patterns.extend(v1_url_patterns)