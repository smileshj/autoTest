#coding = utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime
import random
import re  #正则

profile_directory=r'C:\Users\shj\AppData\Roaming\Mozilla\Firefox\Profiles\g6iqbylc.default'
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
# driver=webdriver.Chrome()
"""
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
#测试random随机点击。火狐52版本运行报错:IndexError: list index out of range
driver.get("https://www.baidu.com")
#driver.implicitly_wait(10)这个等待，火狐52版本不支持，Chrome62正常运行
# driver.implicitly_wait(10)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("kw").submit()
sleep(5)#假设网速良好，火狐等待页面元素加载后再点击
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
"""
#鼠标定位select多选框，修改后保存，火狐版本>47会报错，其它浏览器正常
driver.get("https://www.baidu.com")
mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
#一定要加sleep，否则定位失败
sleep(2)
#xpath定位select下拉框选项
# driver.find_element_by_xpath(".//*[@id='nr']/option[1]").click()
t=driver.find_element_by_xpath(".//*[@id='gxsz']/tbody/tr[2]/td[1]")
print(t.text)
flag1=driver.find_element_by_id("SL_0").is_selected()
if flag1:
    driver.find_element_by_id("SL_1").click()
else:
    driver.find_element_by_id("SL_0").click()
# driver.find_element_by_xpath("//a[@class='prefpanelgo']").click()
#用js代码执行点击操作
js='document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)
#alert()单按钮，dismiss右上角的关闭取消弹出框
driver.switch_to_alert().accept()
"""
"""
#获取一个网页上的带http的链接
url="http://www.cnblogs.com/yoyoketang/"
driver.get(url)
page=driver.page_source
#非贪婪匹配 re.S('.'匹配字符，包括换行符)
url_list=re.findall('href=\"(.*?)\"',page,re.S)
url_all=[]
for url in url_list:
    if "http" in url:
        url_all.append(url)
print(url_all)
"""

#cookie相关操作
"""
#获取cookie，可以通过selenium IDE录制，然后保存为脚本文件
#登录我要自学网
driver.get("http://www.51zxw.net/")
#获取登录前的cookies()
print(driver.get_cookies())
sleep(4)
driver.find_element_by_name("username").send_keys("smileshj")
driver.find_element_by_name("password").send_keys("smileshj")
Select(driver.find_element_by_name("CookieDate")).select_by_visible_text(u"留一天")
driver.find_element_by_css_selector("input.lobtn").click()
sleep(4)
# 获取登录后的cookies()，和登录前对比，多出的就是可以手动添加，然后自动登录的
print(driver.get_cookies())
"""
"""
#登录我要自学网
driver.get("http://www.51zxw.net/")
#添加cookie后自动登录（有可以自动登录的那种）
c6={'name': 'DvForum%5Fwww%2E51zxw%2Enet', 'value': 'userid=14959597&usercookies=1&userhidden=2&password=3M15GsRfey2C3g79&userclass=%B3%F5%C9%FA%D3%A4%B6%F9&username=smileshj&StatUserID=21919751449', 'path': '/bbs/', 'domain': 'www.51zxw.net', 'expiry': None, 'secure': False, 'httpOnly': False}
c7={'name': 'CNZZDATA520717', 'value': 'cnzz_eid%3D1227390813-1511944824-%26ntime%3D1511944676', 'path': '/', 'domain': 'www.51zxw.net', 'expiry': None, 'secure': False, 'httpOnly': False}
c8={'name': 'newsMember', 'value': 'username=smileshj&password=C1C6539BF59DF22D4EA9BAB90F7B2C9E', 'path': '/', 'domain': 'www.51zxw.net', 'expiry': None, 'secure': False, 'httpOnly': False}
driver.add_cookie(c6)
driver.add_cookie(c7)
driver.add_cookie(c8)
sleep(3)
#自动登录了
driver.refresh()
"""
"""
#js控制窗体滚动
driver.get("https://www.taobao.com/")
sleep(3)
#竖向滚动条到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
#元素聚焦
target=driver.find_element_by_xpath("html/body/div[3]/div/ul[1]/li[1]")
driver.execute_script("arguments[0].scrollIntoView();", target)
"""
"""
# print (driver.name)
#浏览器兼容性
#回到顶部
def scroll_top():
    if driver.name=='chrome':
        js = "var q=document.body.scrollTop=0"#这句话对chrome62没有起到效果
    else:
        js="var q=document.documentElement.scrollTop=0"
    return driver.execute_script(js)
#拉到底部
def scroll_foot():
    if driver.name == 'chrome':
        js="window.scrollTo(0,document.body.scrollHeight)"
    else:
        js = "var q=document.documentElement.scrollTop=10000"
    return driver.execute_script(js)
scroll_foot()
sleep(2)
scroll_top()
"""
"""
#去掉元素readOnly属性，以12306网站为例，首次打开需要导入根证书
driver.get("https://kyfw.12306.cn/otn/")
js='document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
#清空文本后再输入值
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2017-11-30")
"""
"""
driver.get("file:///C:/Users/shj/Desktop/div.html")
#竖向滚动条
js1='document.getElementById("yoyoketang").scrollTop=0'
driver.execute_script(js1)
sleep(5)
#横向滚动条，复数
js2='document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js2)
"""
"""
#查看帮助文档，先在DOS命令提示符中输入python -m pydoc -p 8099
#然后在浏览器打开http://localhost:8099/selenium.webdriver.firefox.webdriver.html
"""
import unittest
# c=help(unittest)


class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()
