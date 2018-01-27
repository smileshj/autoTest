
#coding=utf-8
import os
import time
import unittest
from appium import webdriver

#启动配置环境
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['app'] = os.path.dirname(os.path.abspath(__file__))+'\zhihu.apk'

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

time.sleep(2)

