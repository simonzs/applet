import os
import logging
from enum import IntEnum
logging.basicConfig(level=logging.INFO)

class DataType(IntEnum):

    DIR = 1
    FILE = 2


def clear_data(basename: str,
            dirname: str='.', 
            recursive: bool=False,
            _type: DataType=DataType.FILE)：
    if not recursive:
        filepath = os.path.join(dirname, basename)
        if os.path.exists(filepath):
            os.system('rm {} -rf'.format(filepath))
        else:
            logging.warning('{} is not exists'.format(filepath))
    else:
        

            
            