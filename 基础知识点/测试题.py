#11.编写程序，生成包含1000个0到100之间的随机整数，并统计每个元素的出现次数
'''
import random
list01=[]
for x in range(0,10):
    list01+=random.sample(range(0,101),100)
print(list01)
list02=[]
for x in list01:
    if x not in list02:
        list02.append(x)
        t=list01.count(x)
        print(('%d：%d次'%(x,t)),end=' ')
'''

import random
list01=[]
for x in range(0,10):
    list01+=random.sample(range(0,101),100)
print(list01)
for x in range(0,101):
    t=list01.count(x)
    print(('%d：%d次'%(x,t)),end=' ')




#12.编写程序，用户输入一个列表和2个整数作为下标，然后使用切片获取并输出列表中介于2个下标之间的元素组成的子列表。
#   例如用户输入[1, 2, 3, 4, 5, 6]和2,5，程序输出[3, 4, 5, 6]

'''
def xuanqu():
    s=input('请输入一个列表:')
    l=s.split(',')
    l[0],l[-1]=l[0][1],l[-1][0]
    a,b=int(input('请输入两个下标：\n')),int(input(''))
    print('截取后：',l[a:b])
xuanqu()

'''
#13.	编写程序：写一个存书的方法，当用户输入编号和书名，将编号和书名存入到字典中，
#当用户输入over的时候就提示：书添加成功，本次录入完毕。写一个查书的方法，用户输入一个编号就输出对应的书名，
#如果这个编号不存在就提示没有这本书。
'''
book={'001':'爱','002':'恨'}
def cunshu(book):
    while True:
        user=input('请输入编号和书名：')
        l=user.split(',')
        if user=='over':
            print('书添加完毕!')
            break
        book[l[0]]=l[1]
def chashu(book):
    number=input('请输入要查询书的编号：')
    if number in book:
        print('该编号对应书名为：%s'%(book[number]))
    else:
        print('该书不存在！')
cunshu(book)
chashu(book)
'''








#淘宝
'''
gwc={}
i=0
s=0
while True:
    print('\t'*2,'-'*10,'欢迎进入手机淘宝','-'*10,'\n',sep='')
    print(' '*5,'*'*5,'1 登录','*'*5,'\n',' '*5,'*'*5,'2 退出','*'*5,sep='')
    c=input('请选择功能编号：\n')
    if c=='1':
        if i==3:
            print('密码已连续输错三次，不能再登录')
            break
        else:
            account=input('请输入用户名：')
            password=input('请输入密码：')
            if account=='张三' and password=='wasd':
                print('登陆成功')
                while True:
                    print('1.今日特卖\n2.女士服装\n3.男士服装\n4.美食茶酒\n5.结算')
                    c2=input('请选择功能编号：\n')
                    if c2=='1':
                        while True:
                            print('1.毛衫连衣裙 59元\n2.运动鞋 69元\n3.风衣99元')
                            c3=input('请输入要购买的商品编号\n')
                            if c3=='1':
                                gwc['毛衫连衣裙']='59元'
                                yn=input('购买成功，是否继续：y/n')
                                if yn=='n':
                                    print('当前购物车商品有：\n',gwc)
                                    s=input('返回上一级请按n\n')
                                    if s=='n':
                                        break
                            if c3=='2':
                                gwc['运动鞋']='69元'
                                yn=input('购买成功，是否继续：y/n')
                                if yn=='n':
                                    print('当前购物车商品有：\n',gwc)
                                    s=input('返回上一级请按n\n')
                                    if s=='n':
                                        break
                            if c3=='3':
                                gwc['风衣']='99元'
                                yn=input('购买成功，是否继续：y/n\n')
                                if yn=='n':
                                    print('当前购物车商品有：\n',gwc)
                                    s=input('返回上一级请按n\n')
                                    if s=='n':
                                        break
                    elif c2=='4':
                        while True:
                            print('1.咖啡 50元\n2.零食大礼包 49元\n3.柠檬 30元')
                            c3=input('请输入要购买的商品编号')
                            if c3=='1':
                                gwc['咖啡']='50元'
                                yn=input('购买成功，是否继续：y/n\n')
                                if yn=='n':
                                    print('当前购物车商品有：\n',gwc)
                                    s=input('返回上一级请按n\n')
                                    if s=='n':
                                        break
                            if c3=='2':
                                gwc['零食大礼包']='49元'
                                yn=input('购买成功，是否继续：y/n')
                                if yn=='n':
                                    print('当前购物车商品有：\n',gwc)
                                    s=input('返回上一级请按n\n')
                                    if s=='n':
                                        break
                            if c3=='3':
                                gwc['柠檬']='30元'
                                yn=input('购买成功，是否继续：y/n\n')
                                if yn=='n':
                                    print('当前购物车商品有：\n',gwc)
                                    s=input('返回上一级请按n\n')
                                    if s=='n':
                                        break
                    elif c2=='5':
                        print('结算界面\n当前购物车所有商品如下：\n')
                        print(gwc)
                        sum=0
                        for x in gwc:
                            sum+=int(gwc[x][0:-1])
                        print('共消费：',sum)
                        s=input('谢谢使用手机淘宝，继续购物请按w，退出请按0\n')
                        if s=='0':
                            break
                        if s=='w':
                            gwc.clear()
            if account!='张三' or password!='wasd':
                print('用户名或密码输入错误，请重输')
                i+=1
    if c=='2' or s=='0':
        print('退出成功')
        break
'''







