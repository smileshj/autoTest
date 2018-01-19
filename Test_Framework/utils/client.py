"""
添加用于接口测试的client，对于HTTP接口添加HTTPClient，发送http请求
还可以封装TCPClient，用来进行tcp连接，测试socket接口等
"""

import requests
from utils.log import logger

# 定义支持的方法类型
METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']

# 当传入的method的参数不是支持的类型时抛出此异常
class UnSupportMethodException(Exception):
    pass   #有时候我并不在意出现的错误，而是只想让我的程序继续进行下去。

class HTTPClient(object):
    """
    http请求的client，初始化时传入url,method等，可以添加hearders和cookies，但没有auth、proxy。
    举例：HTTPClient('http：//www.baidu.com').send()
    <Response [200]>
    """
    def __init__(self, url, method='GET',headers=None, cookies=None):
        # headers：字典。例如：headers={'Content_Type':'text/html'}，cookies也是字典类型。
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException("不支持的method:{0}，请检查传入参数!".format(self.method))

        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_headers(self, headers):
            if headers:
                self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.headers.update(cookies)

    # *args表示任何多个无名参数，它是一个tuple； ** kwargs表示关键字参数，它是一个dict。并且同时使用 * args和 ** kwargs时，*args参数列要在 ** kwargs前
    def send(self, params=None, data=None, **kwargs):
        response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
        response.encoding = 'utf-8'
        logger.debug('{0} {1}'.format(self.method, self.url))
        logger.debug('请求成功:{0}\n{1}'.format(response, response.text))
        return  response







