"""
#猜数小游戏
import random
#生成随机数
answer=random.randint(1,100)
#玩家输入数值
number=int(input("请输入数字（1-100）："))
#判断输入数字大小
while number!=answer:
    if number>answer:
        number=int(input("大了，请输入数字（1-100）："))
    elif number<answer:
        number=int(input("小了，请输入数字（1-100）："))
#输入数字和生成的随机数相同，游戏结束
print("恭喜你猜对了，数字是：" +str(number))
"""
"""
#读取txt内容
f=open("E:\\Test.txt","r")
lines=f.readlines()
print(lines)
for cids in lines:
    print(cids.split(":")[0])
"""
"""
#读取csv文件，和excel比有看不见的逗号
import csv
csv_file=csv.reader(open("Test.csv","r"))
print(csv_file)
for abc in csv_file:
    print(abc)
#写入csv
stu=["C","c"]
#打开文件
out=open("Test.csv","a",newline="")#把a（追加）换成w就是覆盖最后一行
#设定写入模式
csv_write=csv.writer(out,dialect="excel")
#写入内容
csv_write.writerow(stu)
print("write over!")


from xml.dom import minidom
#加载xml文件
dom=minidom.parse("Testxml.xml")
root=dom._get_documentElement()
# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)
names=root.getElementByTagsName("name")
ages=root.getElementByTagsName("age")
print(names[0].firstChild.data)
print(ages[0].firstChild.data)
#读取属性节点
logins=root.getElementByTagsName("login")
for i in range(2):
    username=logins[0].getAttribute("username")
    password=logins[0].getAttribute("password")
"""

"""
#单线程与多线程
from time import sleep,ctime
import threading
def talk(content,loop):
    for i in range(loop):
        print("start talk: %r" %ctime())
        sleep(2)
def write(content,loop):
    for i in range(loop):
        print("start write: %r" %ctime())
        sleep(3)

threads=[]
t1=threading.Thread(target=talk,args=("Hello,51zxw",2))
threads.append(t1)
t2=threading.Thread(target=write,args=("Life is short,you need python!",2))
threads.append(t2)
if __name__=="__main__":
    for t in threads:
        t.start()
    for t in threads:
        t.join()
print("All the time: %r" %ctime())
#如果是进程，就把threading.Thread替换成mutiprocessing.Process
"""
