#coding = utf-8
# from selenium import webdriver
from appium import webdriver #报错不用管，生成成功的。

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.android.calculator2'
desired_caps['appActivity']='.Calculator'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


# driver.find_element_by_name("1").click()
# driver.find_element_by_name("5").click()
# driver.find_element_by_name("delete").click()
# driver.find_element_by_name("5").click()
# driver.find_element_by_name("+").click()
# driver.find_element_by_name("6").click()
# driver.find_element_by_name("=").click()
# driver.quit()

# 使用appium-desktop录制生成的脚本，稍微顺眼一点吗？
el1 = driver.find_element_by_id("com.android.calculator2:id/digit_7")
el1.click()
el2 = driver.find_element_by_accessibility_id("plus")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit_1")
el3.click()
el4 = driver.find_element_by_accessibility_id("equals")
el4.click()
driver.quit()
