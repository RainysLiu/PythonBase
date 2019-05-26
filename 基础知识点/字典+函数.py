#字典
'''
dic={'李华':86,'李明':96,'张兰':98}
for x in dic:
    print(x)
print('-------------------')
for x in dic.keys():
    print(x)
print('-------------------')
for x in dic.values():
    print(x)
print('-------------------')
for x,y in dic.items():
    print(x,y)
print('-------------------')
dic.update({'张坤':92})
for x,y in dic.items():
    print(x,y)
print('-------------------')
dic.update({'张坤':98})
for x,y in dic.items():
    print(x,y)
print('-------------------')
dic.pop('张坤')
for x,y in dic.items():
    print(x,y)
print('-------------------')
#set类型：只有键，没有键值，其他与字典一样
s=set(dic) #set括号里面必须是列表/元组/字典，不能直接写键
print(s,'\n',type(s))
'''
'''



#判断输入是中文还是英文
def yuyan():
    s=input('请输入一句话(please say a word):')
    i=0
    for x in s:
        if ord('A')<ord(x)<ord('z') or ord(x)==ord(' ') or ord(x)==ord('.') or ord(x)==ord('!'):
            i+=1
    if i==len(s):
        print('你是外国人！')
    else:
        print('你是中国人！')
yuyan()
'''

#德玛西亚
#定义两个技能函数，都传入一个参数当前法力值
'''
def jineng1(f):
    if f>=10:
        print('移动速度增加！攻击造成沉默！德玛西亚！')
        print('当前法力值：%d'%(f-10))
        return (f-10)
    else:
        print('法力值不足，不能释放技能！')
def jineng2(f):
    if f>=20:
        print('我是小陀螺，刷刷刷转起来')
        print('当前法力值：%d'%(f-20))
        return (f-20)
    else:
        print('法力值不足，不能释放技能！')
def game():
    print('人在塔在\n当前法力值为100')
    f=100
    while True:
        if f==0:
            print('法力值消耗为0，程序结束！')
            break
        c=input('请选择你要释放的技能1.德玛西亚2.小陀螺\n')
        if c=='1':
            f=jineng1(f)
        if c=='2':
            f=jineng2(f)
game()
'''



#德玛西亚
#定义一个技能函数，传入两个参数当前法力值和技能选择项

def jineng(f,c):
    if c=='1':
        print('移动速度增加！攻击造成沉默！德玛西亚！')
        return (f-10)
    elif c=='2':
        if f>=20:
            print('我是小陀螺，刷刷刷转起来')
            return (f-20)
        else:
            print('法力值不足，不能释放技能！')
            return f
    else:
        print('输入错误！')
        return f
def game():
    print('人在塔在\n当前法力值为100')
    f=100
    while True:
        if f==0:
            print('法力值消耗为0，程序结束！')
            break
        c=input('请选择你要释放的技能1.德玛西亚2.小陀螺\n')
        f=jineng(f,c)
        print('当前法力值%d'%f)
game()


#方法三：
'''
s1="移动速度增加！攻击造成沉默！德玛西亚！"
s2="我是小陀螺，刷刷刷转起来"
f=100
#定义一个技能释放函数，传入两个技能中所选技能的语句和对应的耗蓝值。
# 功能：打印传入的技能话语，减小该技能对应的蓝量，并打印出减少后法力值多少的语句
def shifang(s,xh):
    global f
    print(s)
    f-=xh
    print("当前法力值：%d"%f)
print("人在他在")
print("当前法力值：%d"%f)
while f>=0:
    if f==0:
        print('法力值消耗为0，程序结束!')
    else:
        print("请选择你要释放的技能1.德玛西亚2.小陀螺")
        bh = int(input())
        if bh == 1:
            shifang(s1, 10)
        elif bh == 2:
            if f>=20:
                shifang(s2, 20)
            if f<20:
                print('法力值不足，不能释放技能')

'''


'''
#局部变量和全局变量的问题
f=100
def mm():    
    print(f-1)   #函数内部可以使用全局变量，但不能更改全局变量。
#   f=f-10     (错误做法，内部未引用，不能更改)     
mm()
def mx():    
    global f       #如果要使用并且改变，需要在函数内部加 global 变量名，进行引用
    f=f-10
    print(f)       
mx()
print(f)
'''