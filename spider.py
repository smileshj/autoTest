
#爬取失败的代码，抄别人的
# coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    image = re.compile(reg)
    imgList = re.findall(image, html)
    x = 0
    for imgurl in imgList:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1

html = getHtml("http://tieba.baidu.com/p/2460150866")

print
getImg(html)

"""
#爬豆瓣的首页
import urllib.request

#网址
url = "http://www.douban.com/"

#请求
request = urllib.request.Request(url)

#爬取结果
response = urllib.request.urlopen(request)

data = response.read()

#设置解码方式
data = data.decode('utf-8')

#打印结果
print(data)

#打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
"""