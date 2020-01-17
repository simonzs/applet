import logging
from typing import types, Any, Dict, List
from functools import wraps
from inspect import isfunction


def check_value(_data: dict, _demo:dict, _keys: list=None) -> list:
    """ check values
    Args:
        _data: the data of check.
        example:

            _data = {
                "name": "123", 
                "password": "456", 
                "id": "789"
            }
        
        _demo: the demo of check
        example:
        
            _demo = {
                "name": "123", 
                "password": "456"
            }
        
        _keys: the keys of need
        example:
        
            _keys = ["name", "password"]
    R
    """
    for k in _keys:
        if _data.get(k) != _demo.get(k):
            raise TypeError('Key: {}, {} != {}'.format(k, _data.get(k), _demo.get(k)))


def check_type(_data: dict, _type: dict):
    """ 
    _data = {"id": "123", "position": {"latitude": 2232.955294, "longitude": 11353.053698}}
    _type = {"id": str, "position": {"latitude": float, "longitude": float}}
    """
    if _data.keys() != _type.keys():
        raise KeyError('The required keys is {}, but the given keys is {}, The difference is {}, The other difference is {}'.format(
                    _type.keys(), 
                    _data.keys(),
                    set(_type.keys()).difference(set(_data.keys())),
                    set(_data.keys()).difference(set(_type.keys()))
                )
            )
    for k, _t in _type.items():
        if isinstance(_data.get(k), dict):
            # 字典, 继续查询
            check_type(_data.get(k), _type.get(k))
        elif not isinstance(_data.get(k), _type.get(k)):
            # 类型不正确, 抛异常
            raise TypeError('Argument <{}> must be {}'.format(k, _type.get(k)))


def typeassert(*args, **kwargs) -> types.FunctionType:

    def decorate(func):
        if not isfunction(func):
            logging.warning("{} is not function".format(func))
            return None
        @wraps(func)
        def wrapper(_object, arg):
            if 'check_type' in kwargs:
                check_type(_data=arg, _type=kwargs.get('check_type'))
            return func(_object, arg)
        return wrapper
    return decorate


def typeassert_func_dict(_type: Dict) -> types.FunctionType:

    def decorate(func: types.FunctionType):
        if not isfunction(func):
            logging.warning("{} is not function".format(func))
            return None
        @wraps(func)
        def wrapper(_input: Dict):
            check_type(_data=_input, _type=_type)
            return func(_input)
        return wrapper
    return decorate


def typeassert_func_list(_type: Dict) -> types.FunctionType:

    def decorate(func):
        if not isfunction(func):
            logging.warning("{} is not function".format(func))
            return None
        @wraps(func)
        def wrapper(_input: List):
            for _item in _input:
                check_type(_data=_item, _type=_type)
            return func(_input)
        return wrapper
    return decorate

input_check = {"id": str, "time": int}

@typeassert(check_type=input_check)
def do_get(a, data):
    return data

def main():
    """
    >>> _data = {"name": "123", "password": "456", "id": "789"}
    >>> _demo = {"name": "123", "password": "456"}
    >>> _keys = ["name", "password"]
    >>> check_value(_data, _demo, _keys)

    >>> _data = {"id": "123", "position": {"latitude": 2232.955294, "longitude": 11353.053698}}
    >>> _type = {"id": str, "position": {"latitude": float, "longitude": float}}
    >>> check_type(_data, _type)

    >>> data = {"id": "123", "time": 123}
    >>> input_check = {"id": str, "time": int}
    >>> @typeassert(check_type=input_check)
    ... def do_get(a, data):
    ...     return data
    >>> do_get(10, data)
    {'id': '123', 'time': 123}
    """

if __name__== "__main__":
    import doctest
    doctest.testmod()