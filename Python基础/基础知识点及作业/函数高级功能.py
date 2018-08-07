#栈和队列


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
#錯誤判斷
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

#map：映射 reduce：归纳



import time
def timetest(i):
    def times():
        t1=time.time()
        i()
        t2=time.time()
        print('程序執行了%s秒'%(t2-t1))
    return times
@timetest
def test():
    time.sleep(1)
    print('花魁')
test()




