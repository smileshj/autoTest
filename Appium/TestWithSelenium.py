#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime
import random

driver=webdriver.Firefox()
"""
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
#加u是python2的写法，因为python3全都改成utf-8了，所以3不需要加u
driver.find_element_by_id("kw").send_keys(u'selesium')
sleep(2)
driver.find_element_by_id("kw").submit()
driver.find_element_by_id("su").click()
driver.get("http://www.163.com")
driver.back()
driver.get("http://www.51zxw.net")
driver.find_element_by_class_name("s_ipt").send_keys("selenium")
driver.close() #关闭当前窗口
driver.quit() #退出浏览器进程

driver.find_element_by_xpath("//input[@id='kw' and @autocomplete='off']").send_keys("selenium")
driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys(" python")
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("selenium")
driver.find_element_by_css_selector("form#form>span>input").send_keys("selenium")
driver.find_element_by_css_selector("input#kw").send_keys("selenium")#csst通过标签与id属性的组合定位
"""
"""
driver.get("http://testerhorde.com")
driver.find_element_by_id("search-button").click()
driver.find_element_by_id("search-term").clear()
driver.find_element_by_id("search-term").send_keys("selenium")
#回车键
driver.find_element_by_id("search-term").send_keys(Keys.ENTER)

driver.find_element_by_id("kw").send_keys("python")
element=driver.find_element_by_id("kw")
driver.maximize_window()
ActionChains(driver).double_click(element).perform()
"""
"""
#显示等待
driver.find_element_by_css_selector("#kw").send_keys("Selenium")
#5秒钟之内每隔0.5秒检测id=su的出现，否则抛出异常。注意了：located里面的参数单独用括号括起来的
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
element.click()
sleep(2)
driver.quit()
"""
"""
# driver.implicitly_wait(5)
#隐式等待
try:
    print(ctime())
    driver.find_element_by_css_selector("#kw").send_keys("selenium")
    driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())
"""
"""
#获取窗口句柄 运行结果报错[WinError 10061] 由于目标计算机积极拒绝，无法连接。
driver.get("https://www.taobao.com/")
#获取当前窗口句柄
h=driver.current_window_handle
# print(h)
#定位所有的元素
s=driver.find_elements_by_css_selector(".search-hots-fline>a")

r=[u"新款连衣裙",u"四件套",u"潮流T恤",u"时尚女鞋",u"短裤",u"半身裙",
   u"男士外套",u"墙纸",u"行车记录仪",u"新款男鞋",u"耳机","时尚女包",u"沙发"]
for a,b in zip(s,r):
    a.click()
    text=a.text
    sleep(2)
    all_h=driver.window_handles
    #循环判断是否与首页句柄相等
    for i in all_h:
        if i !=h:
            driver.switch_to.window(i)
            sleep(1)
    print(driver.title)
    if b in driver.title:
        print(text+u"正常")
    else:
        print(text+u"异常")
    driver.close()
    driver.switch_to.window(h)
    driver.quit()
s[1].click()
all_h=driver.window_handles
print(all_h)
"""
"""
#测试random随机点击，运行报错:IndexError: list index out of range
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("yoyoketang")
driver.find_element_by_id("kw").submit()
s=driver.find_elements_by_css_selector("h3.t>a")
t=random.randint(0,9)
s[t].click()
"""
"""
#定位网易163iframe的登录框
driver.get("http://mail.163.com/")
# iframe=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("123")
driver.find_element_by_name("password").send_keys("456")
driver.switch_to.default_content()
"""