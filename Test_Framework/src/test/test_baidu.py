# import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config,DRIVER_PATH

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    #URL = "http://www.baidu.com"
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

    #定义搜索id（firebug获得元素ID）
    locator_kw = (By.ID,'kw')
    locator_su = (By.ID,'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        #连接驱动，打开浏览器
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self):
        print("dsf1")
        # self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys("selenium")
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_element(*self.locator_result)#result是：WebElement (session="4deefab86ff7db61db83d4223ae700f3", element="0.03811039743044686-3")>，不可迭代即不可for循环。
        print(links)
        # for link in links:
        #     print(link.text)


    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys("Python")
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_element(*self.locator_result)
        print(links)

if __name__ == '__main__':
    unittest.main()