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

    # def __init__(self,):

