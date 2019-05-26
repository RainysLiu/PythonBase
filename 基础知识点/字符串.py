#字符串切片
'''
a = 'abcdef'
print(a[0:4:2])
'''

#求列表中的元素最大最小值
'''
l=[1,5,6,45,68,5,4,5,556,41,98,45,32,15,68,48,15,69]
min=l[0]
max=l[0]
for x in range(len(l)):
    for y in l:
        if y<min:
            min=y
        if y>max:
            max=y
print('max=%d min=%d'%(max,min))
'''
#分离字符串
'''
s='sam aim send\tssd dff\n kmiu\t ksks\n kkk'
print(s.split())
'''

#统计字符串字母出现个数
#给定一个字符串，求字符串中所有字符出现的次数
'''
s='我爱你！我真的爱你！我真的非常爱你！我确认真的非常特别爱你！'
#m=[]
for x in range(len(s)):
    i=0
    for y in s:
        if y==s[x]:
            i+=1
#            if i>1:
#                m.append(s.index(y))
#    else:
    print(('"%s"：%d次'%(s[x],i)),end='  ')
#print(m)

'''



#输入一个字符串，求字符串中所有字符出现的次数，不能重复
#s='我爱你！我真的爱你！我真的非常爱你！我确认真的非常特别爱你！'
'''
s=str(input('请输入任意一个字符串：'))
m=[]
for x in range(0,len(s)):
    if s[x] in m:
        pass
    else:
        t=s.count(s[x])
        if t>1:
            m.append(s[x])      
        print(('"%s":%dtimes'%(s[x],t)))

'''


'''
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
print ("列表反转后: ", list1)
'''


#将A--H八个人随机分配到编号办公室1--3的办公室，然后打印出每个办公室分配了几个人
'''
import random
offices=[[],[],[]]
names=['A','B','C','D','E','F','G','H']
for tempname in names:
    i=random.randint(0,2)
    offices[i].append(tempname)
print(offices)
i=1
for x in range(0,len(offices)):
    l=len(offices[x])
    print('房间%d有%d个人'%(i,l))
    i+=1
'''



'''
#小明坐公交或者地铁
d=float(input('请输入小明每天上班公里数：'))
t=int(input('请输入小明每个月上班天数：'))
c=input('请选择小明的交通方式（1.公交 2.地铁）：')
if c=='1':
    m=0
    if d<=10:
        m=2
    else:
        if d%5==0:
            m=2+(d-10)/5
        else:
            m=2+(d-10)//5+1
    m=0.5*2*m*t
    print('====================================\n小明一个月乘公交上下班共花费%.1f元'%m)
elif c=='2':
    m=0
    if d<=6:
        m = 3
    elif d<=12:
        m = 4
    elif d<=22:
        m = 5
    elif d<=32:
        m = 6
    else:
        if (d-32)%20==0:
            m = 6+(d-32)/20
        else:
            m = 6+(d-32)//20+1
    m=2*m*t
    if m<=100:
        m = m
    elif m<=150:
        m = (m-100)*0.8+100
    elif m<=400:
        m = (m-150)*0.5+50*0.8+100
    else:
        m = (m-400)+250*0.5+50*0.8+100
    print('========================\n小明一个月乘地铁上下班共花费%.1f元'%m)
'''








    

