#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ip.py
@Time    :   2020/01/16 10:01:18
@Version :   1.0
@Desc    :   The tool of ip.
'''

import socket
from IPy import IP
from urllib.parse import urlparse as base_urlparse
from subprocess import getstatusoutput

def is_ip(address: str):
    try:
        IP(address)
        return True
    except Exception as e:
        return False 

def iptype(value:str) -> str:
    """
    Return whethr or not given value is a valid ip.
    If the value is valid ip name this function returns ``True``, otherwise False
    :param value: ip string to validate.
    """
    if not is_ip(value):
        raise ValueError("{} is not ip address".format(value))
    return IP(value).iptype()

def is_valid_domain(value):
    try:
        socket.gethostbyname(value)
        return True
    except Exception as e:
        return False

def is_reachable(host, timeout=1):
    cmd = 'ping -c 1 -w {_timeout} {_host}'.format(_timeout=timeout, _host=host)
    exitcode, _ = getstatusoutput(cmd)
    if exitcode == 0: # 1 成功
        return True
    elif exitcode == 1: # 0 失败
        return False
    return False


def urlparse(url):
    """Parse a URL into 6 components:
    """
    return base_urlparse(url)


def main():
    """
    >>> is_ip("127.0.0.1")
    True
    >>> is_ip("127.0.0.256")
    False
    >>> iptype("192.168.1.1")
    'PRIVATE'
    >>> is_reachable("www.baidu.com")
    True
    >>> is_reachable("192.168.0.1")
    False
    >>> o = urlparse("http://www.baidu.com:10/api/v2/overview?limit=5&offset=0")
    >>> o.scheme
    'http'
    >>> o.netloc
    'www.baidu.com:10'
    >>> o.path
    '/api/v2/overview'
    >>> o.query
    'limit=5&offset=0'
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()