#字符串处理

str1 = 'hello'
str2 = 'baby'
str3=str1+str2  #字符串拼接
print(str3)
print(str3*5)  #多次重复
#下标/索引
print(str3[0:9])
#判断字符是否在字符串  
print('e' not in str3)
print('e' in str3)
#大小写转换
str4 = 'Sokj jJKK mlKin oPNM Njmm'
print(str4.lower())
print(str4.upper())
#大小写取反
print(str4.swapcase())
#首字母大写，其余小写
print(str4.capitalize())
#将每个单词的首字母大写，其余小写
print(str4.title())
#字符查找输出下标,find没有输出-1，index没有会报错
print(str4.find('3'))
#print(str3.index('3'))
#切片
print(str4[3:])
#字符串替换
print(str4.replace('m','哎',2))
#判断是否以某个字符串开头
str4.startswith('m')
#制定字符在字符串中出现的次数
str4.count('m')
#其他：

#center指定宽度居中
#ljust/rjust自定宽度左右对齐
'''
#按指定字符或字符串拆分，拆分后输出列表，制定字符串去掉
print(str4.split('m'))
str5='wo\nai\nni\na'
print(str5.split())
print(str5.splitlines())
#以‘，’为分割的形式连续输入五个数字的字符串，然后求平均数
m=input('please input 5 number,split with ",":')
l=m.split(',')
s=0
for x in l:
    s+=int(x)
print(s/(len(l)))
'''

#列表的简单处理
'''
list01 = [14,'25','NIHAO','STR']
list01.append('min')
list01.extend('strr')  #添加多个元素 
print(list01.count('25'))
list01.pop(2)        #根据指定下标删除
list01.remove('STR')  #根据指定元素删除
list01[0]=12
print(list01)
print(list01.index('min'))   #求指定元素下标
list02=[1,2,3,9,5,4,7]
list02.sort()
print(list02)
list02.reverse()
print(list02)

'''


#值类型和引用类型：
#仅整形、浮点型、布尔型为值类型，其他都为引用性
#值类型赋值，引用型赋地址
#整数为值类型
'''
a=3
b=a
b=10
print(a,b)
#列表为引用型
l1=[2,9,10,8,3,8,7]
l2=l1.copy()   #若不想改表原来列表，则用copy函数
l2.sort()
print(l1,l2)
l2=l1
l2.sort()
print(l1,l2)
'''


#键盘输入几个值，输出第二大的值
'''
m=input('please input 5 number,sep with ",":')
l=m.split(',')
s=[]
for x in l:
    s.append(int(x))
s.sort()
print(s[-2])
'''


#元组tuple
'''
tuple01=(1,2,3,5)
'''

#字典dict
#如果键重复，后面的元素会覆盖前面
'''
dic={'zhang':85,'li':82,'wang':'96','li':86}
print(dic)
#增删修改
dic['zhang']=86
print(dic)
dic.pop('li')
print(dic)
'''


#作业
#1.删除列表中重复的元素

#删除后面重复的
'''
s=['s','m','s','w','q','m','r','t','q','j','s','w','m']
print('原列表为：  ',s)
m=[]
s2=[]
for x in s:
    if x in m:
        pass
    else:
        if s.count(x)>1:
            m.append(x)      
        s2.append(x)
s=s2
print('删除重复后：',end=' ')
print(s)
'''
'''
s=['s','m','s','w','q','m','r','t','q','j','s','w','m']
s2=[]
for x in s:
    if x not in s2:
        s2.append(x)
print(s2)
'''


#删除前面重复的
'''
s=['s','m','s','w','q','m','r','t','q','j','s','w','m']
print('原列表为：  ',s)
s2=s.copy()
m=[]
for x in range(0,len(s)):
    if s[x] in m:
        s2.remove(s[x])
    else:
        if s.count(s[x])>1:
            m.append(s[x]) 
s=s2 
print('删除重复后：',end=' ')
print(s)
'''




#2.输入姓名存入列表
'''
l=[]
while True:
    s=input('请输入一个学生姓名：')
    l.append(s)
    if s=='张三':
        print('录入结束！已录入的学生共%d人，信息如下：'%(len(l)))
        print(l)
        break
'''

#用列表录入学生姓名
'''
a=['liuang']
p=['110']
while True:
    c=input(('1.登录\n2.注册\n3.退出\n请选择：'))
    if c=='1':
        print('欢迎来到登录界面！')
        account=input('请输入用户名：')
        password=input('请输入密码：')
        if account in a:
            i=a.index(account)
            if password==p[i]:
                print('登陆成功！')
            else:
                print('密码错误!')
        else:
            print('账户不存在！')
    elif c=='2':
        print('欢迎来到注册界面！')
        account=input('请输入用户名：')
        password=input('请输入密码：')
        a.append(account)
        p.append(password)
        print('注册成功！')
            
    elif c=='3':
        print('退出成功！')
        break
'''


#用字典
'''
a={'杨伟':'10086'}
while True:
    c=input(('1.登录\n2.注册\n3.退出\n请选择：'))
    if c=='1':
        print('欢迎来到登录界面！')
        account=input('请输入用户名：')
        password=input('请输入密码：')
        if account in a:
            if password==a[account]:
                print('登陆成功！')
            else:
   ,,   ,          print('密码错误!')
     , ,  else:
            print('账户不存在！')
    elif c=='2':
        print('欢迎来到注册界面！')
        account=input('请输入用户名：')
        password=input('请输入密码：')
        a[account]=password
        print('注册成功！')       
    elif c=='3':
        print('退出成功！')
        break
'''
#从前往后冒泡
n=[9,4,6,2,1,7,8,6,3,4,2,1]
for x in range(len(n)):
    for y in range(0,len(n)-x-1):
        if n[y+1]<n[y]:
            n[y],n[y+1]=n[y+1],n[y]
print(n)

#从后往前冒泡
n=[9,4,6,2,1,7,8,6,3,4,2,1]
for x in range(len(n)):
    for y in range(len(n)-1,x,-1):
        if n[y-1]>n[y]:
            n[y],n[y-1]=n[y-1],n[y]
print(n)

#插入排序
s=[9,4,6,2,1,7,8,6,3,4,2,1]
for x in range(1,len(n)):
    for y in range(0,x-1):
        if s[y]>s[x]:
            s.insert(y,s[x])
            s.pop(x+1)
print(s)

