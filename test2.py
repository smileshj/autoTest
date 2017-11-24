#coding = utf-8
"""
for a in range(0,11):
    print (a)
#循环中可以使用序列解包
d={'x':1,'y':2}
for key,value in d.items():
    print (key,"=",value)

#zip函数可以把两个序列“压缩”在一起，返回一个元组的列表，当短的序列用完会停止,短的写在前面。
names=['zhao','qian','sun','li']
ages=[22,34,23]
zip(ages,names)

while True:
    word=input("please enter a word：")
    if not word:break
    print(word)
del函数，当x,y指向同一个列表，删除（del）x不会影响y。因为删除的只是名称，不是列表本身（值）。
scope={}#命名空间
scope['x']=2
eval ('x*x',scope)  #求值

#记录函数，相当于给方法写注释。用#号或在第一行直接写文档字符串。
def square(x):
    'dsfd0'
    return x*x
print (square.__doc__)#访问文档字符串。双下划线方法是特殊属性
help(square)#查看某方法的注释
#*收集剩余的所有参数，单星号或双星号都可以使用。返回元组
def a(titile,*ds):
    print(titile)
    print(ds)
a('c:',1,2,3,4)

**关键字参数的“收集”操作，返回字典
举例：
def print_params(x,y,z=3,*pos,**key):
print x,y,z
print pos
print key
print_params(1,2,3,5,6,7,foo=1,bar=2)
1 2 3
(5,6,7)
{'foo':1,'bar':2}
"""
"""
import wx
app=wx.App()
frame=wx.Frame(None,title="sss")
frame.Show()
btna=wx.Button(frame,label="a",pos=(255,5))
btnb=wx.Button(frame,label="b",pos=(315,5))
app.MainLoop()
"""
"""
#窗体按钮绑定事件
import  wx
def hello(event):
    print("hello world")
app=wx.App()
frame=wx.Frame(None,title="Hello,Python!",size=(200,100))
btn=wx.Button(frame,label="hello")
btn.Bind(wx.EVT_BUTTON,hello)
frame.Show()
app.MainLoop()
"""
#抛出异常
def devision(x,y):
    if y==0:
        raise ZeroDivisionError("零不能做除数！")
    return x/y
try:
    devision(8,0)
except BaseException as msg:
    print(msg)