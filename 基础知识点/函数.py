
#函数的参数
#1.位置参数:按顺序调用参数即可
# def s1(a,b):
#     pass


# 2. 默认参数
# def s2(a,b=2):
#     print(a+b)
# s2(1)

# 3.不定长参数
'''
def s3(b,*a):
    if b=='he':
        s=0
        for x in a:
            s+=x
        print(s)
    if b=='ji':
        s = 1
        for x in a:
            s *= x
        print(s)
# def s4(*a):
#     print(sum(a))
s3('he',2,6,4,8,6,1,5)
s3('ji',2,6,4,8,6,1,5)
'''

#兔子程序
#递归函数
# month=int(input('请输入月份:'))
# def rabbit(month):
#     if month==1 or month==2:
#         return 1
#     else:
#         return (rabbit(month-1)+rabbit(month-2))
# print('共有兔子：%d只'%(rabbit(month)))

#循环用列表
# s=[]
# x=0
# while x<=month-1:
#     if x==0 or x==1:
#         s.append(1)
#     elif x>1:
#         s.append(s[x-1]+s[x-2])
#     x+=1
# print('共有兔子：%d只'%(s[x-1]))
#
# #循环交换值
# a,b=1,1
# for x in range(1,20+1):
#     if x<=2:
#         c=1
#     else:
#         c=a+b
#         b=a
#         a=c
# print(c)

#递归求阶乘

# def jiecheng(n):
#     if n==1:-+
#         return 1
#     else:
#         return (jiecheng(n-1)*n)
# print(jiecheng(5))

#递归函数：函数里面自己调用自己，也算是循环
'''
def jiecheng(n):
    if n==1:
        return 1
    return (jiecheng(n-1)*n)
print(jiecheng(5))
'''


#文件处理
#1.打开文件
#2.读/写文件
#3.关闭文件


#用程序将10.txt从C:\Users\Rainy\Desktop\拷贝到F:\
'''
import os
path1='C:/Users/Rainy/Desktop/10.txt'
with open(path1, 'r') as f:
    s=f.read()
    print(s)
print('---------------------')

path2='F:/10.txt'
f=open(path2,'w')    #open函数在打开目录中进行检查，如果有则打开，否则新建
f.close()
with open(path2,'w') as f:
    f.write(s)
with open(path2,'r') as f:
    print(f.read())

'''

#作业
'''
#1.生成指定长度验证码
import random
def yanzhengma(l):
    list01 = [chr(x) for x in range(97, 123)] + [str(x) for x in range(0, 10)] + [chr(x) for x in range(65, 91)]
    yzm=''
    if l<4:
        l=4
    for x in range(l):
        yzm+=random.choice(list01)
    print(yzm)
yanzhengma(10)


def yzm(l):
    list01=[chr(x) for x in range(97,123)]+[str(x) for x in range(0,10)]+[chr(x) for x in range(65,91)]
    print(''.join(random.sample(list01,l)))
yzm(10)



#2.返回一个文件的格式
def geshi(s):
    for x in range(len(s)-1,0,-1):
        if s[x]=='.':
            print('文件名后缀为%s' % (s[x:]))
            break
geshi('2.5.txt')


def geshi(s):
    l=s.split('.')
    print('后缀名为.%s'%(l[-1]))
geshi('2.5.txt')



#3.求出列表中第一二大的数
#先排序，后取最大和次大

l=[2,6,4,8,7,9,4,6,6,6,9,5,8,4,7,1,5,4,8,7,5,6,9,1,4,]
def zuida(l):
    l.sort()
    t=l.count(l[-1])
    print('最大为%d，次大为%d' % (l[-1], l[-1-t]))
zuida(l)



def zuida(l):
    max1=max(l)
    l2=[]
    for y in l:
        if y!=max1:
            l2.append(y)
    max2=max(l2)
    print('最大值为%d，次大值为%d'%(max1,max2))
zuida(l)


'''


