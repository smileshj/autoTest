
#coding=utf-8
import os
import time
import unittest
from selenium import webdriver

#启动配置环境
desired_caps={
    'platformName':'Android',
    'deviceName':'360 N4',
    'platformVersion':'6.0',
    'appPackage':'com.taobao.taobao',
    'appActivity':'com.taobao.tao.homepage.MainActivity3',
    #屏蔽手机软键盘，直接输入中文，改完要把手机默认输入法设置回去
    'unicodeKeyboard':True,
    'resetKeyboard':True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
time.sleep(2)
#搜索界面的输入框
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"苹果")
