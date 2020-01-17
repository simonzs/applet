# -*- encoding: utf-8 -*-
'''
@File    :   run.py
@Time    :   2019/11/27 11:30:06
@Author  :   Simon 
@Version :   1.0
@Desc    :   None
'''

import logging
import tornado
from tornado.options import options
from app.settings import settings
from app.urls import url_patterns

class TornadoApplication(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)
        self.executor = tornado.concurrent.futures.ThreadPoolExecutor(16)

def main():
    app = TornadoApplication()
    app.listen(options.port)
    logging.info("start service at: {}".format(options.port))
    try:
        tornado.ioloop.IOLoop.current().start()
    finally:
        logging.info("stop service")
        