#1-100奇偶数之和之和
'''
s1=0
s2=0
n=0
while n<=100:
    if n%2==1:
        s1+=n
    if n%2==0:
        s2+=n
    n+=1
print('奇数之和：%d 偶数之和：%d'%(s1,s2))
'''

#求阶乘
'''
s=1
n=1
while n<=10:
    s*=n
    n+=1
print(s)
'''

#水仙花数
'''
num=100
i=0
l=[]
while num<1000:
    ge=num%10
    shi=num//10%10
    bai=num//100
    if ge**3+shi**3+bai**3==num:
        l.append(num)
        i+=1
    num+=1
print(l,i)
'''

#回文数
'''
num=10000
while num<100000:
    num=str(num)
    ge=int(num[4])
    shi=int(num[3])
    bai=int(num[2])
    qian=int(num[1])
    wan=int(num[0])
    if ge==wan and shi==qian and ge+shi+wan+qian==bai:
        print(num)
    num=int(num)
    num+=1
'''

#9*9乘法表
'''
x=1
while x<=9:
    y=1
    while y<=x:
        print(('%d*%d=%d'%(x,y,x*y)),end=' ')
        y+=1
    print()
    x+=1
'''


#打印*号
'''
x=5
n=x
while x>=1:
    w=1
    while w<=n-x:
        print(' ',end='')
        w+=1
    y=1
    while y<=2*x:    
        print('*',end='')
        y+=1
    print()
    x-=1
x=5
n=x
while x>=1:
    w=0
    while w<x-1:
        print(' ',end='')
        w+=1
    y=n
    while y>=x:    
        print('**',end='')
        y-=1
    print()
    x-=1
'''


#数学函数max min应用
'''
import random
n=1
l=[]
while n<=10:
    r=random.randint(1,100)
    l.append(r)
    n+=1
print(l)
print('max=%d min=%d'%(max(l),min(l)))
'''  


#数学函数
'''
import math
print(pow(2,3)),print(abs(-9))
a=math.pi
print(math.tan(a/4))
print(math.sqrt(4))
'''




#随机数
'''
import random
s='loveisforever'
a=random.choice(s)  #从列表中随机一个数
print(a)
print([x for x in s])
'''



#作业
#1.键盘猜三次数字
'''
import random
r = random.randrange(1,99)
i=0
for x in range(3):
    n = int(input('请输入1--100内的两位数：'))
    if n==r:
        print('恭喜！你猜对了！')
        break
    elif n<r:
        print('你猜小了！')
        i+=1
    elif n>r:
        print('你猜大了！')
        i+=1
if i==3:
    print('不好意思，机会完了！')
'''


#循环输入五个数字，求平均值
'''
i=1
s=0
while i<=5:
    n=float(input('请输入数字：'))
    if n<0:
        print('输入为负，程序结束')
        break
    s+=n
    i+=1
if i==6:
    print('平均数为：',s/5)
'''

#珠穆朗玛峰叠纸
'''
h=0.01
i=0
while h<=8848:
    h*=2
    i+=1
print('需要折叠次数：',i)
'''

#小芳存钱
'''
s=0
i=0
while s<=100:
    i+=1
    s+=2.5
    if i%5==0:
        s-=6
print(i)
'''

