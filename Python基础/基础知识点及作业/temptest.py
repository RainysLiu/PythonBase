

#
# import requests,re,os
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
#     }
# param = {'page':1}
# base_url = 'https://www.doutula.com/photo/list/'
# PICTURES_PATH = os.path.join(os.getcwd(), 'doutu/')
#
#
# def get_page(page):
#     urls = []
#     for x in range(1,page + 1):
#
#         param['page'] = x
#         urls.append(requests.get(base_url,params=param,headers = headers).url)
#     return urls
#
# def get_imagelist(url):
#     html = requests.get(url,headers = headers).text
#     reg = r'data-original="(.*?)".*?alt="(.*?)"'
#     reg = re.compile(reg,re.S)
#     imagelist = re.findall(reg,html)
#     return imagelist
#
# def get_picture(imagelists):
#     try:
#         os.mkdir(PICTURES_PATH)
#     except:
#         pass
#     for x in imagelists:
#         content = requests.get(x[0],headers = headers).content
#         # print(content)
#         picture_path = os.path.join(PICTURES_PATH,x[1] + '.jpg')
#         with open(picture_path, 'wb') as f:
#             f.write(content)
#
# urls = get_page(10)
# for x in urls:
#     imagelist = get_imagelist(x)
#     get_picture(imagelist)



'''
print(type('slksjck'))
a=1
if type(a)==int:
    print('比好')
print(ord('z'))
'''

'''
from PIL import Image
im=Image.open('C:\\Users\Rainy\Pictures\Camera Roll\WIN_20180620_09_49_10_Pro.jpg','r')
print(type(im))
print(im.format,im.size,im.mode)
'''

#多态：前提必须要多重继承，多重继承的子类拥有相同父类属性才能实现多态
# 给人写一个功能为喂动物类，狗和猫属于动物类，然后人每次喂动物时只需要传入动物的子类就能实现喂动物
# class animal(object):
#     def __init__(self,name,food):
#         self.name=name
#         self.food=food
#     def eat(self):
#         print(('%s'%self.name)+'吃'+('%s'%self.food))
# class dog(animal):
#     def __init__(self,name,food):
#         super(dog, self).__init__(name,food)
# class cat(animal):
#     def __init__(self,name,food):
#         super(cat, self).__init__(name,food)
# class person(object):
#     def __init__(self,name):
#         self.name=name
#     def feed(self,animal):
#         print('%s给%s%s'%(self.name,animal.name,animal.food))
#         animal.eat()
# class chicken(animal):
#     def __init__(self):
#         self.name='长安鸡'
#         self.food='虫子'
# def main():
#     dog1=dog('长安狗','骨头')
#     cat1=cat('长安猫','鱼儿')
#     chicken1=chicken()
#     p1=person('刘昂')
#     p1.feed(dog1)
#     p1.feed(cat1)
#     p1.feed(chicken1)
#
# if __name__ == '__main__':
#     main()


#类属性
'''
class person():
    name='李华'

print(person.name)
p1=person()
print(p1.name)
p1.name='张明'
print(p1.name)
'''



# 其它要点：

#1.动态添加属性和功能




#2.限制实例属性,不能动态添加
#在属性初始化前加上__slots__=元组
#元组里面放的元素才可以添加，否则不行


#3.将私有的属性变为外部可访问
# @property和@属性名.setter将私有属性分别可直接get和可改变
#


'''
#7.2讲课内容
#栈和队列
'''

#栈
#python没有真正的栈,只能用list模拟栈的存储，特点：先进后出，压栈存入，弹栈取出

#队列
#特点：先进先出

# import collections
# q=collections.deque()
# q.append(10)
# q.insert(1,20)
# q.append(30)
# print(q)
# print(q.popleft())

#匿名函数
#lambda：功能

#返回函数
#将函数当做参数传递

'''
def run():
    print('在跑')
def shout():
    print('在叫')
def eat():
    print('在吃')
def animal(animal,*f):
    for i in f:
        print(animal,end='')
        i()
animal('长安',run,shout,eat)
'''


#自定义函数str2int实现字符串转整形
#map和reduce
'''
import functools
digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(strs):
    return functools.reduce(lambda x,y:x*10+y,map(lambda s:digits[s],strs))
print(type(str2int('123456')))
print(str2int('123456'))




#固定参数，原函数参数被固定
def summ(a,*b,c=10):
    b=list(b)
    sumb=sum(b)
    print(a+sumb+c)
summ(1,2)
summ(1,20,c=20)
#偏函数，原函数不做更改
summ2=functools.partial(summ,c=30)
summ2(1,50,20,50,84,75,c=80)
summ2(1,50,c=80)

#filter函数,筛选器
def oushu(n):
    return n%2==0
print(list(filter(oushu,range(1,100))))


#sorted整理，可以传入key属性，按属性进行整理
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
'''
#装饰器
#用一个函数对另一函数进行功能添加
'''
def zhaungshi(i):
    def betiful(s):
        print('*******')
        i(s)
        print('*******')
    return betiful
@zhaungshi
def items(s):
    print('%s'%s)
items('锦上添花')
'''


'''
异常处理
报错依然执行
'''
'''
print('开始')
try:
    print(int('执行'))
except :
    print('语法错误')
else:
    print('没找到错误原因')
print('结束')
'''

#map和reduce的中文意思
'''
map：映射 reduce：归纳
'''



#作业：一个列表，列表中存储字符串，将字符串首字母大写，其余小写
'''
def fun(s):
    return s.capitalize()
l=['sx dAFc','ad aDa','skjJ kKk Ll']
print(list(map(fun,l)))
'''

#电话号码判断
'''
import re
def checkMobile(strData):
    CMCCRule=r"^(13[4-9]|15[0-2]|15[7-9]|18[2,3,7,8]|147)\d{8}$"
    CCrule=r"^(13[0,1,2,6]|18[5,6]|145)\d{8}$"
    Cnetrule=r"^(133|153|18[0,1,9])\d{8}$"
    rescmcc = re.findall(CMCCRule,strData)
    rescc=re.findall(CCrule,strData)
    rescnet=re.findall(Cnetrule,strData)
    if rescmcc:
        print('%s是中国移动号码'%strData)
    elif rescc:
        print('%s是中国联通号码'%strData)
    elif rescnet:
        print('%s是中国电信号码'%strData)
    else:
        print('这不是一个手机号码')
checkMobile('15257450512')
'''


'''
7-3讲课内容
'''
#单元测试:可以对类、函数、模块进行测试
import unittest




#迭代器
'''
from collections import Iterable
#检测是否为可迭代对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

iter=iter(range(1,11))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
while True:
    try:
        print(next(iter))
    except:
        print('结束啦')
        break
print(iter)
'''
#生成器:yeild
'''
def add1(x):
    while True:
        x+=1
        yield  x
a=add1(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(a)
'''
'''
#排列与组合
import itertools
randomliter=itertools.permutations([1,2,3,4],2)
list01=list((randomliter))
print(list01)
print(len(list01))
randomliter=itertools.combinations([1,2,3,4],2)
list01=list((randomliter))
print(list01)
print(len(list01))
randomliter=itertools.product([1,2,3,4],repeat=2)
list01=list((randomliter))
print(list01)
print(len(list01))
randomliter=itertools.product([1,2,3,4],repeat=3)
list01=list((randomliter))
print(list01)
print(len(list01))
'''


#作业
#1.写邮箱
'''
import re
def checkEmail(strData):
    emailrule="^[\w-]{1,}@[\da-zA-Z]{2,}\.(com|COM)$"
    rescmcc = re.findall(emailrule,strData)
    if rescmcc:
        print('%s是一个邮箱'%strData)
    else:
        print('这不是一个邮箱！')
checkEmail('liu@163.COM')
'''







#2.看网络编程TCP和UDP
'''
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
'''



#7.5號講課内容
'''
#赋值、浅拷贝和深拷贝
import copy
list1=[1,2,3,4,['a','b','c','d',[1,5,4]]]
print(list1)
list2=list1
list3=list1.copy()
list4=copy.deepcopy(list1)
list1.append(6)
list1.insert(2,2)
list1[-2].insert(-1,66)
print(list1)
print(list2)
print(list3)
print(list4)
'''


'''
s1='dfgbnmjhiyjurr'
s2=s1
s1='655+656+55+'
print(s1,s2)
'''

'''
s='adc'
a=s
s=s+'sss'
print(a,id(a))
print(s,id(s))


a=1
b=a
a=3
print(a,id(a))
print(b,id(b))

#赋值、浅拷贝和深拷贝
import copy
l1=[1,2,4,5,6,[1,2,3]]
print(l1,id(l1))
l2=l1
l3=l1.copy()
l4=copy.deepcopy(l1)
print(l3,id(l3))
l1.insert(2,3)
l1[-1].insert(-1,4)
print(l1,id(l1))
print(l2,id(l2))
print(l3,id(l3))
print(l4,id(l4))

#汉字可做变量
薛長安 = 99
賀磊磊 = 100
print(薛長安)
print(賀磊磊)

print(repr('strss'))
print(type(repr('strss')))
print('strss')
print(type('strss'))

print(ord('x'))

'''




#请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
'''
x=list(range(100))
print(x)
i=0
x2=[]
while i<=len(x):
    x2.append(x[i:i+3])
    i+=3
x=x2
print(x)
#请写出一段 Python 代码实现删除一个 list 里面的重复元素
# x=[1,1,2,2,3,4,4,6,6,5,5,7,7,8,9,9,]
# x2=[]
# for i in x:
#     if i not in x2:
#         x2.append(i)
# x=x2
# print(x2)
print(list(set([1,1,2,2,3,4,4,6,6,5,5,7,7,8,9,9,])))
'''

#设计实现遍历目录与子目录,抓取.pyc 文件
'''
import os
filenumber=0
def wenjian(path):
    global filenumber
    lists=os.listdir(path)
    for x in lists:
        path2=os.path.join(path,x)
        if os.path.isfile(path2):
            if x[-4:]=='.pyc':
                print('%s是.pyc文件     位置：%s'%(x,path2))
                filenumber+=1
        else:
            wenjian(path2)
    return filenumber
wenjian('F:\Rainy\workspace')
print('當前目錄有.pyc文件%d個'%(filenumber))

#写出一个函数,给定参数 n,生成含有 n 个元素值为 1~n 的数 组,元素顺序随机,但值不重复
import random
n=20
numberlist=random.sample(range(1,n+1),n)
print(numberlist)
#在不用其他变量的情况下，交换a、b变量的值
a,b=1,2
a,b=b,a
#如何在一个 function 里设置一个全局变量
a=1
def jia():
    global a
    a=a+1
    return a
print(jia())
#檢測下面函數功能

a='25'
print(id(a))
print((a).isdigit)
'''
s='sss sss jbgvg hvgb'
s=s.replace(' ','%20')
print(s)
class Solution:
   def replaceSpace(self,s):
       print(s.replace(' ','%20'))
s=Solution()
s.replaceSpace('hello python fdf dfd ')