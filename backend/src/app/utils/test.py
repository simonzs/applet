import inspect
import re
import time
import json
import logging
logging.basicConfig(level=logging.DEBUG)

class Person(object):

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def toJSON(self):
        return {"name": self.name, "age": self.age, "city": self.city}

def wdp(_variable):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 堆栈的最里层是该打印函数,获取上一层的调用故取第二层堆栈
    exec_info = inspect.stack()[1]
    fn = exec_info.filename

    # 所在行
    _line = exec_info.lineno
    # 调用的方法
    _function = exec_info.function

    # 执行的命令
    _cmd = exec_info.code_context[0]
    print(_cmd)

    # 执行的命令中参数的名称
    pattern = re.compile(
        wdp.__name__ + '\((.*?)\)$',
        re.S
    )
    _cmd = _cmd.strip().replace('\r', '').replace('\n', '')
    # 变量名
    vn = re.findall(pattern, _cmd.strip())[0]

    # 变量转字符串
    
    if hasattr(_variable, "toJSON"):
        info = _variable.toJSON()
    elif hasattr(_variable, "__str__"):
        info = _variable.__str__()
    else:
        info = str(_variable)
    log_info = '[{time}] [{filename}] [{func}] [{line}] {variable_name} = {variable}'.format(
        time=t,
        filename=fn,
        func=_function,
        line=_line,
        variable_name=vn,
        variable=info
    )
    print(exec_info.code_context)
    print(exec_info.count)
    print(exec_info.filename)
    print(exec_info.frame)
    print(exec_info.function)
    print(exec_info.index)
    print(exec_info.lineno)
    print(info)
    print(log_info)

if __name__ == '__main__':
    p = Person("wbq", 25, "bj")
    wdp(p)
