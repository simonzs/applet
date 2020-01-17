# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2019/11/27 11:31:34
@Author  :   Simon 
@Version :   1.0
@Desc    :   基础Handler类
'''
import json
import base64
import logging
import requests
import tornado.web

from Crypto.Cipher import AES
from tornado import iostream
from tornado.web import StaticFileHandler

from app.settings import settings
# from app.v1.driver.casbin import casbin
from app.v1.utils.attime import get_current_time_ms
from app.v1.models import userticket


def encrypt(key, uid, timestamp):
    def uid2message(uid, timestamp):
        ret = "{}/{}/jx".format(uid, timestamp)
        aim_length = int(len(ret) / 16) * 16 + 16
        return ret + (" " * (aim_length - len(ret)))
    try:
        obj = AES.new(key, AES.MODE_CBC, 'default salt 16b')
        return obj.encrypt(uid2message(uid, timestamp))
    except TypeError:
        obj = AES.new(key.encode('utf-8'), AES.MODE_CBC, 'default salt 16b'.encode('utf-8'))
        return obj.encrypt(uid2message(uid, timestamp).encode('utf-8'))


def decrypt(key, message):
    def message2uid(text):
        if isinstance(text, bytes):
            text = str(text, encoding='utf-8')
        return tuple(text.strip().split("/"))
    try:
        obj = AES.new(key, AES.MODE_CBC, 'default salt 16b')
    except TypeError:
        obj = AES.new(key.encode('utf-8'), AES.MODE_CBC, 'default salt 16b'.encode('utf-8'))
    return message2uid(obj.decrypt(message))


def calc_ticket(uid, timestamp):
    key = settings.get("cookie_secret")
    return encrypt(key, uid, timestamp)


class BaseHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('hello world!')

    def get_current_uid(self):
        return self.current_uid

    def set_current_uid(self):
        self.current_uid = None
        cookie = self.get_cookie(settings["login_cookie"])
        if cookie is None:
            return None
        t = base64.b64decode(cookie)
        _, _, token = decrypt(settings["cookie_secret"], t)
        if token != "jx":
            return False
        self.current_uid = 123
        return True

    def clear_login_cookies(self):
        self.clear_cookie(settings.get("login_cookie"))

    def set_login_cookie(self, uid):
        now = get_current_time_ms()
        login_cookie = settings.get("login_cookie")

        ut_object = userticket.Data.get_by_user_id(user_id=uid)
        if not ut_object:
            data = {
                "user_id": uid,
                "ticket": calc_ticket(uid, now),
                "timestamp": now,
            }
            ack, ut_id = userticket.Data.create_one(data)
            if ack:
                ut_object = userticket.Data.get_by_user_id(user_id=uid)
                ticket = ut_object.ticket
            else:
                ticket = data.get("ticket")
        else:
            ticket = ut_object.ticket
        self.set_cookie("jiangxing_login_ticket", "BzuMEBf5ypjPwinvwGtngMKZyDvK2C+3ww1+jAgr7WzNA0EnDy2HqOTZG/eUVF9ESjst8cfDrM4uu/YUlzVQxg==", expires_days=3) # HACK
        self.set_cookie(login_cookie, base64.b64encode(ticket), expires_days=3)


    # def prepare(self):
    #     status_cookie = self.set_current_uid()
    #     url = self.request.path
    #     if status_cookie is None:
    #         if not casbin.enforce("visitor", url, self.request.method):
    #             return self.login_failed()
    #     else:
    #         if not status_cookie:
    #             self.clear_login_cookies()
    #             return self.login_failed()
    #         else:
    #             if not casbin.enforce(self.userinfo.role, url, self.request.method):
    #                 return self.access_failed()


    def parse_json_body(self):
        try:
            if isinstance(self.request.body, bytes):
                data = str(self.request.body, encoding='utf-8')
            else:
                data = self.request.body
            if not data:
                return {}
            self.request_data = json.loads(data)
        except (KeyError, ValueError) as e:
            self.write_error(500, "bad json format: {}".format(str(e)))
            self.request_data = None
        return self.request_data

    def parse_query_arguments(self):
        ret = {}
        for k, v in self.request.query_arguments.items():
            if isinstance(v, list) and len(v) != 0:
                if isinstance(v[0], bytes):
                    ret[k] = str(v[0], encoding='utf-8')
                else:
                    ret[k] = v[0]
            else:
                ret[k] = v
        return ret

    def finish_request(self, body):
        self.write(json.dumps(body, sort_keys=True, separators=(',', ': ')))
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.finish()

    def write_success_json(self, data=None):
        self.set_status(200)
        if data is None:
            return self.finish_request({"desc": "success", "data": ""})
        else:
            return self.finish_request({"desc": "success", "data": data})

    def login_failed(self):
        self.write_error(499, "bad login user: login failed")

    def access_failed(self):
        self.write_error(403, "you do not have permission to access this page")

    def write_error(self, status_code, desc=None, reason=None, **kwargs):
        result = {}
        if reason:
            self.set_status(status_code, reason=reason)
        else:
            self.set_status(status_code)
        if desc is None and "exc_info" in kwargs:
            desc = str(kwargs["exc_info"][1])
        result['desc'] = desc
        return self.finish_request(result)


    def create_static_file_handler(self, name, path):
        self.set_header("Content-Type", "application/octet-stream")
        self.set_header("Content-Disposition", "attachment; filename={}".format(name))
        content = StaticFileHandler.get_content(path)
        if isinstance(content, bytes):
            content = [content]
        for chunk in content:
            try:
                self.write(chunk)
                yield self.flush()
            except iostream.StreamClosedError:
                self.write_error(500, desc="download file failed, retry")
                return
        self.set_status(200)
        return self.finish()


class AsyncHandler(BaseHandler):

    def success(self, result=None):
        return 200, result

    def failed(self, status_code, result=None):
        return status_code, result

    def write_success(self, result):
        return self.write_success_json(result)

    @property
    def executor(self):
        return self.application.executor

    @tornado.gen.coroutine
    def async_worker(self, func, data):
        # 监控每一个接口的速度
        status, result = yield self.executor.submit(func, (data))
        if status == 200:
            return self.write_success(result)
        else:
            return self.write_error(status, result)

    def do_post(self, data):
        return self.failed(404, "no implement")

    def do_put(self, data):
        return self.failed(404, "no implement")

    def do_get(self, data):
        return self.failed(404, "no implement")

    def do_delete(self, data):
        return self.failed(404, "no implement")

    def post(self):
        data = self.parse_json_body()
        return self.async_worker(self.do_post, data)

    def put(self):
        data = self.parse_json_body()
        return self.async_worker(self.do_put, data)

    def get(self):
        data = self.parse_query_arguments()
        return self.async_worker(self.do_get, data)

    def delete(self):
        data = self.parse_query_arguments()
        return self.async_worker(self.do_delete, data)


class ProxyHandler(AsyncHandler):

    def post(self):
        self.do_post(None)
        return self.async_worker(self.do_proxy, requests.post)

    def put(self):
        self.do_put(None)
        return self.async_worker(self.do_proxy, requests.put)

    def get(self):
        self.do_get(None)
        return self.async_worker(self.do_proxy, requests.get)

    def delete(self):
        self.do_delete(None)
        return self.async_worker(self.do_proxy, requests.delete)

    def set_proxy_url(self, url):
        self.proxy_url = url

    def write_success(self, result):
        self.write_error(200, result)

    def write_error(self, status, result):
        self.set_status(status)
        self.write(result)
        self.finish()

    def do_proxy(self, func):
        try:
            url = self.proxy_url
        except:
            return self.failed(404, "not found proxy url")
        timeout = settings.get("proxy_timeout", 20)
        if hasattr(self, 'timeout'):
            timeout = self.timeout
        try:
            query_args = self.parse_query_arguments()
            if self.request.body:
                res = func(url=url, data=self.request.body, headers=self.request.headers,
                           timeout=timeout, params=query_args)
            else:
                res = func(url=url, headers=self.request.headers, timeout=timeout, params=query_args)

            for k in res.headers:
                if k.lower() == "transfer-encoding" and res.headers[k].find("chunked") != -1:
                    continue
                self.set_header(k, res.headers[k])
            # send raw data with status_code, maybe rename func
            return self.failed(res.status_code, res.content)
        except Exception as e:
            logging.exception(e)
            self.clear()
            return self.failed(502, "proxy error: {}".format(e))


class ServiceProxyHandler(ProxyHandler):

    def initialize(self):
        self.service = None

    def post(self, url=""):
        self.set_proxy_url("{}{}".format(self.service, url))
        return self.async_worker(self.do_proxy, requests.post)

    def get(self, url=""):
        self.set_proxy_url("{}{}".format(self.service, url))
        return self.async_worker(self.do_proxy, requests.get)

    def put(self, url=""):
        self.set_proxy_url("{}{}".format(self.service, url))
        return self.async_worker(self.do_proxy, requests.put)

    def delete(self, url=""):
        self.set_proxy_url("{}{}".format(self.service, url))
        return self.async_worker(self.do_proxy, requests.delete)
