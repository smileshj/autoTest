# import os
import io #Python2是StringIO
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import  HTMLTestRunner
from utils.mail import Email
from src.test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'
    #URL = "http://www.baidu.com"  #直接写路径
    #定义读取driver的路径
    #abspath是当前脚本的绝对路径，路径带文件本身，dirname返回的是不带文件本身的路径，即文件所在路径
    #print(os.path.abspath(__file__))   #E:\Program\pythonProject\Test_Framework\src\test\test_baidu.py，去别就是后面有没有\test_baidu.py
    # base_path = os.path.dirname(os.path.abspath(__file__))+'\..\..'#加的'\..\..'起到的效果是向上返回两层
    # print(base_path)
    # driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')
    # print(driver_path)

    #os.path.split(path)将path分割成目录和文件名二元组返回
    #获取当前运行脚本的绝对路径（去掉最后2个路径）
    #path3 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    #print(path3)

    """
    配置了PageObjecth后注释掉此段，common的browser、page，还有page的baidu_main_page.py和baidu_result_page.py
    #定义搜索id（firebug获得元素ID）
    locator_kw = (By.ID,'kw')
    locator_su = (By.ID,'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')]
    """

    def setUp(self):
        #普通方式连接驱动，打开浏览器
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
        # self.driver.get(self.URL)
        #PageObject方式，初始页面是main page，传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def tearDown(self):
        # self.driver.quit()   #普通方式退出
        self.page.quit()       #PageObject方式退出

    """
    #每搜索不同的文字，就要写一个重复的代码
    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys("selenium")
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_element(*self.locator_result)#result是：WebElement (session="4deefab86ff7db61db83d4223ae700f3", element="0.03811039743044686-3")>，不可迭代即不可for循环。
        # print(links)
        logger.info(links)
        # for link in links:
        #     print(link.text)


    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys("Python")
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_element(*self.locator_result)
        # print(links)
        logger.info(links)
    """

    """
    subTest是Python3 unittest里带的功能，PY2中没有，PY2中要想使用，需要用unittest2库。
    subTest是没有setUp和tearDown的，所以需要自己手动添加并执行。
    把要搜索的内容，存储在其它的文件中（比如excel文件），参数化读取

    def test_search_2(self):
        datas = ExcelReader(self.excel).data
        print(datas)
        for d in datas:
            with self.subTest(data=d):
                self.setUp()
            self.driver.find_element(*self.locator_kw).send_keys(d['search'])#此处的search是title_line
            self.driver.find_element(*self.locator_su).click()
            time.sleep(2)

            links = self.driver.find_element(*self.locator_result)
            logger.info(links)
            self.tearDown()
    """
    # 用了PageObject后的写法
    def test_search_3(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.setUp()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  #页面跳转到result page
                links = self.page.result_links
                logger.info(links)
                self.tearDown()


if __name__ == '__main__':
    #verbosity=0（静默模式），100个用例，失败20，成功80，=1（默认）,失败的用例前面有个‘F’,成功的用例前面有个“.”,=2（详细）,每个用例的相关信息
    # unittest.main(verbosity=2)   #不带测试报告运行，但是如果添加了日志，可以生成日志。
    #看看report的效果，在配置的report目录下是否有html报告生成,真的生成了，在浏览器中打开就看到了。
    report = REPORT_PATH + '\\report.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架', description='修改测试报告')
        runner.run(TestBaiDu('test_search_3')) #传入类名和方法名

    # 发送邮件
    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请注意查收。',
              receiver='2594911454@qq.com',
              server='smtp.163.com',
              sender='zgongzs@163.com',
              password='',
              path=report
              )
    e.send()