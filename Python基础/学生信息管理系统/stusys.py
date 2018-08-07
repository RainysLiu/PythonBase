###python studentsinfosys.py
import os
import pickle
import time
#判断字符串是否都是汉字的函数
def isallCHN(s):
    for c in s:
        if not('\u4e00' <= c <= '\u9fa5'):
            return False
    return True
# total_students={'001':{'姓名':'李华','年龄': 18, '籍贯': '四川', '联系电话': '18706774188'},
#  '002':{'姓名':'刘宇','年龄': 30, '籍贯': '北京', '联系电话': '158756421587'},
# '003':{'姓名':'李强','年龄': 15, '籍贯': '南京', '联系电话': '1524154875'},}
#实现在字典中插入输入的学生信息的函数
def add(total_students):
    while True:
        n=str(input('请输入学生姓名：'))
        if isallCHN(n)==True:
            break
        else:
            print('输入的不是中文名，请重输！')
    while True:
        a=input('请输入学生年龄：')
        if len(a)<=2 and a.isdigit()==True:
            break
        else:
            print('输入的年龄有误，请重输！')
    while True:
        p = str(input('请输入学生籍贯：'))
        if isallCHN(p) == True:
            break
        else:
            print('输入的不是中文，请重输！')
    while True:
        t=str(input('请输入电话：'))
        if len(t)==11 and a.isdigit()==True:
            break
        else:
            print('输入的电话号码有误，请重输！')
    listnumber=[]
    for x in total_students.keys():
        listnumber.append(int(x))
    m='00'+str(max(listnumber)+1)
    total_students[m]={'姓名':n,'年龄':a,'籍贯': p, '联系电话': t}
    print('该同学的信息添加成功，学号为%s'%m)
#实现在字典中删除输入的学生信息的函数
def dell(total_students):
    n=str(input('请输入要删除的学生学号：'))
    if n in total_students:
        print('该学生信息如下：\n',end='')
        print(total_students[n])
        c=input('确认删除请按1 放弃请按任意其它键\n')
        if c=='1':
            del total_students[n]
            print('删除成功!')
        else:
            print('您已放弃删除！')
    else:
        print('该学号找不到！')
#实现在字典中查找输入的学生对应的信息并打印
def search(total_students):
    n=str(input('请输入要查找的学生学号：'))
    if n in total_students:
        print('你要查找的学生信息如下：\n',end='')
        print(total_students[n])
    else:
        print('该学号找不到！')
#读取文件的函数
def openfile():
    filepath = os.path.join(os.getcwd(), 'studentlist.txt')
    f = open(filepath, 'rb')
    return pickle.load(f)
    f.close()
#写入文件的函数
def writefile(t):
    filepath = os.path.join(os.getcwd(), 'studentlist.txt')
    f = open(filepath, 'wb')
    pickle.dump(t, f)
    f.close()
#主函数
def stusys():
    total_students=openfile()
    password = '110'
    while True:
        print("****************************\n",
            '欢迎进入XXXX学生管理系统!\n1.添加学生信息\n2.删除学生信息\n3.查找学生信息\n4.查看当前系统所有学生信息\n5.退出系统',
            '\n****************************')
        a=str(input('请选择:'))
        if a=='1':
            add(total_students)
            while True:
                print("*********\n1.返回\n2.继续添加\n*********")
                b=str(input('请输入:'))
                if b=='2':
                    add(total_students)
                elif b=='1':
                    break
                else:
                    print('输入有误！')
            writefile(total_students)
        elif a=='2':
            s=str(input('请输入系统密码：'))
            if s==password:
                dell(total_students)
                while True:
                    print("*********\n1.返回\n2.继续删除\n*********")
                    b = str(input('请选择:'))
                    if b == '2':
                        dell(total_students)
                    elif b == '1':
                        break
                    else:
                        print('输入有误！')
            else:
                print('系统密码输入错误！')
        elif a=='3':
            search(total_students)
            while True:
                print("*********\n1.返回\n2.继续查找\n*********")
                b=str(input('请选择:'))
                if b=='2':
                    search(total_students)
                elif b=='1':
                    break
                else:
                    print('输入有误！')
        elif a=='4':
            s=str(input('请输入系统密码：'))
            if s==password:
                print('请稍候...')
                time.sleep(2)
                print('查询成功！该学生信息系统所有学生信息如下：')
                for x,y in total_students.items():
                    print(x,y)
                while True:
                    s=input('返回主界面请按0\n')
                    if s=='0':
                        break
                    else:
                        print('输入有误！')
            else:
                print('系统密码输入错误！')
        elif a=='5':
            print('正在保存学生信息并退出系统！请稍候...')
            writefile(total_students)
            time.sleep(2)
            break
        else:
            print('输入有误！')
stusys()
