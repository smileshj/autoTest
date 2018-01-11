import random
#创建一个宽度为2，高度为52的数组
#这种创建方式(浅复制即副本和原来的一起变)会导致结果全部是['方块',‘k’]因为是一个list数组*52份，列表是可变的，列表只是复制引用，所以改变列表的元素会影响所有引用对象
poker=[[0]*2]*52
#第一种改法：这里是一个(0,0)元组序列和字符串，是不可变的，。深复制即副本变了，不影响原来的元组，会创建新的元组
# poker=[([0]*2) for i in range (52)]

color=''
num=0

for i in range(0,4):
    for j in range(0,13):
        if i==0:
            color='黑桃'
        elif i==1:
            color='红心'
        elif i==2:
            color='梅花'
        elif i==3:
            color='方块'

        poker[num][0]=color

        if j==0:
            poker[num][1]='A'
        elif j==10:
            poker[num][1]='J'
        elif j==11:
            poker[num][1]='Q'
        elif j==12:
            poker[num][1]='K'
        else:
            #带符号的十进制整数替换
            poker[num][1]='%d'%(j+1)
            
        #print(poker[num],num+1)
        #第二种方法，直接从内部改变赋值方式:
        poker[num]=[color,poker[num][1]]

        num=num+1

print(poker)


# 洗牌
random.shuffle(poker)
print('洗牌')
for i in range(0,len(poker)):
    print(poker[i])