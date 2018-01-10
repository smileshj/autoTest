#coding = utf-8
"""# from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.find_element_by_id("kw").send_keys('自动化测试')
"""
#  import math
# print (int((math.pow(2,3))))
# print (int(2.6))
# print (2**3)
# if 1==1: print("one equals one")
# name = input("What is your name?")
# print("hello，"+name+"!")
"""print (r'''ddd
ab
dd
dd
''')"""
#ctrl+/代表批量用#注释，取消注释也是一样的
#print (r"Let's go")
"""序列分为列表、字符串和元组。列表可变，字符串和元组不可变。
类表和元组和索引示例
months=['January','February','March','April','May','June','July','August','Septemper','October','November', 'December']
endings=['st','nd','rd']+17*['th']\
    +['st','nd','rd']+17*['th']\
    +['st']
year=input("Year:")
month=input("month(1-12):")
day=input("Day[1-31]:")
month_number=int(month)
day_number=int(day)
month_name=months[month_number-1]
ordinal=day+endings[day_number-1]
print(month_name+' '+ordinal+'.'+year)
"""
"""分片
numbers=[1,2,3,4,5,6]
numbers[1:2] #结果是[2]因为从索引0开始编号，冒号为分隔，冒号前面的包含，后面的不包含在分片中。
numbers[-2:]#结果是[4,5,6]就是倒数，然后一直到最后。
numbers[:3]#结果是[1,2,3],就是正数，索引从第一个0的数字1，到索引为2的3数字3截止。
numbers[:]#结果就是整个序列。
#第三个参数：分片的步长
numbers[0:4:5] #1,2,3,4,5中，每隔5个数取一次值。运行结果就只有1.步长可以是负数，从右到左取值numbers[4:0:-5],结果是5。
"""
"""序列成员资格示例
database=[['a','1'],['b','2'],['c','3'],['d','4']]
username=input("username:")
pin=input("pin code：")
if[username,pin] in database:print ("yes")

list('hello')#序列改成列表
x=[1,2,3]
x[1]=4 #列表元素赋值
del x[2] #删除列表元素
#分片赋值增加
numbers=[1,5]
numbers[1:1]=[2,3,4]
#分片赋值减少
numbers=[1,2,3,4,5]
numbers[1:4]=[]
numbers.append(6)  #返回的还是原来的列表a
numbers.count(6)
c=[7,8,9]
numbers.extend(c) #extend只是修改了原来的列表。列表a+列表b返回一个全新的列表(效率低)
numbers[len(numbers):]=c #这样也可以，不会修改原列表，但是代码可读性低。
numbers.index('2')
numbers[1]
numbers.insert(3,"four")#将对象插入到列表中
numbers[3:3]=["four"]#insert的操作用分片赋值实现。
#pop()方法介绍：会先移除掉列表元素，然后返回被移除的值。相当于出栈（LIFO后进先出拿碗碟）队列就是地铁排队出去，先进到队伍先出去
x=[1,2,3]
x.pop()#返回值为3，此时x=[1,2]
x.pop(0)#返回值为1，此时x=[2]
x.remove(2)#remove移除列表的值，没有返回值。
list(reversed(x))#反向迭代序列，只返回一个迭代器对象，用list()函数把返回的对象转换成列表。
a=[3,1,5]
b=a
b.sort()#此时a和b都指向[1,3,5]，不好可以用分片复制，y=x[:] y.sort()  #列表.sort()返回值为None
#或者用sorted()，两者内容一样，但是占用两个空间
y=sorted(x)

x=['a','abxxxxxxxx','abcddd','abcde','abcd']
x.sort(key=len)#按长度排序从小到大
x=[4,1,5]
x.sort(reverse=True)#按大小反向排序，结果是从大到小。
#元组，用逗号分隔了一些值，就创建了元组，大部分是用()圆括号括起来的。例如（40，）。区别是不可变序列
tuple([1,2,3]) #把一个序列作为参数转换为元组，参数是元组原样返回。
x=1,2,3
x[0:2]#结果是（1，2）
"""
"""
格式化字符串操作符%，转换说明符%s(s表示值会被格式化为字符串)，如果整个要转换的字符串（如format）中有百分号，要写成两个%%
format="hello,%s,%s enough for ya%%?"
values=('world','Hot')
print (format % values)
#格式化实数（浮点数），可以用f说明符类型，一个句点加上希望保留的小数位数加上类型字符
x=('圆周率：%.12f')
from math import pi
print (x % pi)
#另一种格式化值的方法：模板字符串，传参替换，用$。美元符号就两个$$。替换单词的一部分，参数名要用括号括起来
from string import Template
a=Template('$x，这是$x，$$，It\'s sel${x}nium!')
a.substitute(x="e")
#用字典变量提供值/名称对
b=Template('A $a and $b')
d={}
d['a']='a'
d['b']='b'
b.substitute(d)
#find方法寻找字符串中的字符串。join方法是split的逆方法
seq=['1','2','3']
a='+'
a.join(seq)#结果是‘1+2+3’
dirs='','usr','bin','env'
'/'.join(dird)#结果是'/usr/bin/env'
print ('c:'+'\\'.join(dirs))#结果是c:\usr\bin\env
"that's all.".title()#结果是That'S All.
import string
string.capwords("that's all.")#结果是That's All.
#replace()查找并替换。split()分隔符。strip方法返回去除左侧和右侧（不包含内部）空格的字符串，如果要指定去除的字符，比如*号，放到括号中当做参数即可。strip('*')
translate()函数。string.maketrans(from，to),创建用于转换的转换表。
创建字典的三种方法：字典中的键是唯一的，值并不唯一。字典的好处：不用像序列一样一定要在序号范围内插入，可以任意加到字典的某个位置中。
#（1）键值对
test={'1':'a','2':'b','3':'c','4':'d'}
#（2）dict函数（不是真正的函数，是像list,tuple,str一样的类型）
items=[('name','xiaoxue'),('age',18)]
d=dict(items) #d的值{'age':18,'name':'xiaoxue'}
#（3）dict函数通过关键字参数创建字典，不带参数则返回一个新的空字典{}。
d=dict(name='xiaoxue',age=18)#d的值{'age':18,'name':'xiaoxue'}
dict.fromkeys(['name','age'])结果是{'age':None,'name':None}
或dict.fromkeys(['name','age'],'X')结果是{'name':'X','age':'X'}#X是自定义的值。
copy函数（浅复制）返回的是一个相同键-值对的新字典，副本替换值f['a']='x'，原来不受影响。副本修改比如remove/append一个，原来的也会改变。c.copy()
deepcopy函数（深复制）用法：deepcopy(d),结果就是原来的怎么变化都不会影响副本。
from copy import deepcopy
#get方法，如果访问字典中不存在的项会报错，如d['who'],但是print d.get('who')得到None。还可以替换None，d.get('who','X')，get()如果键存在就是查对应的值
#dictionary.has_key(''),返回False or True
#pop('键')，移除指定键的元素并显示出来。popitem()一个接一个地移除并处理项可以用。字典是没有顺序的概念的。
#字典的update()方法，相同则替换，不同则添加，d1={'x':'1','y':'2'}  d2={'x':'3','f':'5'} d1.update(d2)
#d={'x':'1','y':'2'}  d.values(）#结果是dict_values(['1','2'])

#x,y,z=1,2,3#同时給多个变量赋值，也叫序列解包
dic={'name':'sunny','bf':'x'}
key,value=dic.popitem() #就是key='bf',value='x'
#增量赋值：x+=1，*=，/=,%=都适用，对其他数据类型也适用，比如字符串。只要二元运算符本身适用于这些数据类型即可。
#bool('')==bool(0)==bool([])==False 但它们本身并不相等
if x=1: elif x=2: esle
#python中双等号判断两个对象是否相等，用 x is y 判断两者是否为同一个对象。
#字符串可以按照字母顺序排列进行比较,序列也可以‘Ad’.lower()<'ba' True  #[2,[1,4]]<[2,[1,5]]
"""






