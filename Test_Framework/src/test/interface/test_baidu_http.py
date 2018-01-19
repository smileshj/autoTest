import unittest
from utils.config import Config, REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode

"""
如果你的接口类型不是HTTP的，请自己封装对应的Client类。
socket库测TCP接口、suds库测SOAP接口，不论你是什么类型的接口，总能找到对应的Python库的。
"""
class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url = self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        #断言(检查点)，就是判断实际结果是否和预期结果一致
        assertHTTPCode(res, [200])
        self.assertIn('百度一下，你就知道', res.text)

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从零开始搭建测试框架')
        runner.run(TestBaiDuHTTP('test_baidu_http'))
