# 类和实例
'''
class Student(object):
    def __init__(self, name, score,):
        self.name = name
        self.score = score
#        self.grade = get_grade(self.score)
    def get_grade(self):
        if self.score >= 90:
            return '优秀'
        elif self.score >= 60:
            return '一般'
        else:
            return '不行'
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
sime = Student('sime',59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
print(sime.name, sime.get_grade())
'''

'''
class pai:
    huase = ''
    shuzi = 0


# 实例化两个牌
pai1 = pai()
pai2 = pai()
# 给两张牌1和牌2赋予花色和数字的属性
pai1.huase = '黑桃'
pai1.shuzi = '1'
pai2.huase = '红桃'
pai2.shuzi = '2'
class ren:
    l=''
    r=''
    def qupai(self,x,y):
        global r,l
        l=x
        r=y
        print(l,r)
    def huanpai(self):
        global l,r
        l,r=r,l
        print(l,r)
# 实例化人
ren1 = ren()
# 让人1进行取换牌行为
ren1.qupai(pai1.huase+pai1.shuzi,pai2.huase+pai2.shuzi)
ren1.huanpai()

'''


'''
#人开枪射击
class mans:
    def fire(self,zi):
            zi-=1
            print('开火成功,当前剩余子弹%d'%zi)
class guns:
    zidan=0
man=mans()
gun=guns()
gun.zidan=10
man.fire(gun.zidan)

'''

#构造函数
'''
class Person:
    def __init__(self,name,age):
        #要写类的属性就在构造函数中用self去创建
        self.name=name
        self.age=age
    def show(self):
        print('姓名：%s 年龄:%d'%(self.name,self.age))
#创建对象时会自动调用构造函数
p1=Person('王麻子',20)
p1.show()
'''




#析构函数
# 在变量销毁的时候是会执行的
# 1.程序执行完毕自动销毁
# 2.可用del手动销毁
# 3.如果变量在函数内部使用，那么该函数执行完毕时，该变量会销毁
'''
class Person:
    def __init__(self,name,age):
        #要写类的属性就在构造函数中用self去创建
        self.name=name
        self.age=age
        print('姓名：%s 年龄:%d' % (self.name, self.age))
    def __del__(self):
        print('我死了')
# p1=Person('李华',18)
'''
# 2.可用del手动销毁
'''
p1=Person('李四',20)
for x in range(6):
    print(x)
    if x==5:
        del p1    #用del手动销毁
        break
#print(p1.name)   #对象已经销毁 无法再使用
'''
#3.如果变量在函数内部使用，那么该函数执行完毕时，该变量会销毁
'''
def fun():
    print('start')
    p1 = Person('王麻子', 20)
    for x in range(6):
        print(x)
    print('end')
fun()
'''

#函数重写
#
# class Person:
#     def __init__(self,name,age,sex,nation,height,weight):
#         #要写类的属性就在构造函数中用self去创建
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.nation=nation
#         self.height=height
#         self.weight=weight
    # def __str__(self):
    #     return '姓名：%s 年龄：%d 性别：%s 民族：%s 身高：%.2f 体重：%.2f'%\
    #            (self.name,self.age,self.sex,self.nation,self.height,self.weight)
    # def __repr__(self):     #__repr__只在 __str__不存在时起作用
    #     return '陌生人你好！'
# p1=Person('王五',16,'男','汉',1.87,68)
# print(p1)



#重载

#重写和重载的区别
#重写：把底层的代码重新写一遍
#重载：python里没有重载，其他语言同名函数会根据参数不同去寻找
#覆盖：python中同名函数，后面的会覆盖前面





#射击问题
'''

class DanJia:
    def __init__(self,bulletCount):
        self.bulletCount=bulletCount

class Gun:
    def __init__(self,danjia):
        self.danjia=danjia
    def shoot(self):
        #子弹数量减少
        if self.danjia.bulletCount<=0:
            #添加子弹  装弹
            print("该装弹了!")
            return 0
        else:
            self.danjia.bulletCount -= 1
            print("发射子弹，剩余数量%d" % self.danjia.bulletCount)
            return 1
class Person:
    def __init__(self,gun):
        self.gun=gun

    def fire(self):
        #枪发射子弹
        self.gun.shoot()
        if self.gun.shoot()==0:
            p1.zhuangdan(5)
    def zhuangdan(self,n):
        self.gun.danjia.bulletCount+=n
        print('装弹%d发成功！'%n)

#创建弹夹
dj=DanJia(5)
#创建一把枪
g=Gun(dj)
#创建一个人
p1=Person(g)
p1.fire()
p1.fire()
p1.fire()
p1.fire()
p1.fire()
p1.fire()
p1.fire()
'''


#访问限制,不能直接访问,只能本类使用
'''
class person:
    def __init__(self,age):
        self.__age=age    #该属性限制访问
    def changeage(self,a):  #自身定义函数可以间接访问和修改
        self.__age=a
    def show(self):
        print('年龄：%s'%self.__age)
p1=person(5)
p1.show()
p1.changeage(50)
p1.show()
'''


#类与对象练习
'''
class cat:
    def __init__(self,name,age,clour):
        self.__name=name
        self.__age=age
        self.__clour=clour
    def run(self):
        print('%s在跑'%self.__name)
    def call(self):
        print('%s在叫'%self.__name)
    def show(self):
        print('名字：%s 年龄：%s 颜色：%s'%(self.__name,self.__age,self.__clour))
    def getage(self):
        return int(self.__age)
    def getname(self):
        return self.__name
cats=[]
def creatcat():
    for x in range(3):
        n,a,c=input('请输入猫的名字：'),input('请输入猫的年龄：'),input('请输入猫的颜色：')
        simplecat=cat(n,a,c)
        cats.append(simplecat)
def catShowRunCall():
    sage=0
    for y in cats:
        print('**********猫的信息如下*********')
        y.show()
        y.run()
        y.call()
        sage+=y.getage()
    print('三只猫总共%d岁'%sage)
def serachcat():
    while True:
        name=input('请输入要查询的猫名字：\n')
        i=0
        for x in cats:
            if name==x.getname():
                x.show()
            else:
                i+=1
        if i==3:
            print('没有这只猫！')
            break
creatcat()
'''

#作业
#1.账户中注册
'''
class users:
    def __init__(self,account,password,sex):
        self.account=account
        self.password=password
        self.sex=sex
    def show(self):
        print('你输入的信息如下：')
        print('姓名：%s 密码：%s 性别：%s'%(self.account,self.password,self.sex))

def SignIn():
    while True:
        a = input('请输入用户名：\n')
        if 64<ord(a[0])<123:
            break
        else:
            print('用户名必须以字母开头，请重输！')
    while True:
        p = input('请输入密码：\n')
        if len(p)<=6:
            print('密码必须大于六位，请重输！')
        else:
            break
    while True:
        s = input('请输入性别：\n')
        if s=='男' or s=='女':
            break
        else:
            print('性别输入错误，请重输！')
    user=users(a,p,s)
    user.show()
SignIn()
'''

#英雄类
'''
class heros:
    def __init__(self,Pnumber,hp,atk,Pname):
        self.Pnumber=Pnumber
        self.hp=hp
        self.atk=atk
        self.Pname=Pname
    def atkway(self,name1,name2):
        self.hp[name1]-=self.atk[name2]
        print('玩家%s受到了玩家%s的%d点伤害，剩余hp为%d'%(name1,name2,self.atk[name2],self.hp[name1]))
    def enter(self,name):
        (self.Pname).append(name)
        self.Pnumber+=1
        (self.hp)[name]=200
        print('玩家%s进入游戏，当前玩家%d人'%(name,self.Pnumber))
hero=heros(Pnumber=0,hp={},atk={'tom':5,'lucy':10,'mack':15},Pname=[])

hero.enter('tom')
hero.enter('lucy')
hero.enter('mack')
hero.atkway('tom','lucy')
hero.atkway('tom','mack')
hero.atkway('mack','tom')
hero.atkway('lucy','mack')
hero.atkway('tom','lucy')
hero.atkway('tom','mack')

'''

'''
class cars():
    def __init__(self,oillevel,speed):
        self.oillevel=oillevel
        self.speed=speed
    def show(self):
        print('新手上路，当前时速为：%d，当前油量为：%d'%(self.speed,self.oillevel))
    def zhuanwan(self):
        self.speed=20
        self.oillevel-=1
        self.show()
    def zhhixing(self):
        self.speed+=10
        self.oillevel-=1
        self.show()
    def stop(self):
        print('停车')
car=cars(100,10)
car.zhhixing()
car.zhhixing()
car.zhuanwan()
car.zhhixing()
car.stop()
'''



#单继承和多继承
'''
class Person():
    # 构造函数有参数的情况
    # 子类必须给父亲构造函数赋值

    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

    # 构造函数无参的
    # 子类也必须调用父亲的构造函数
    
    def __init__(self):
        self.name = ""
        self.age = 0
        print("父亲")

    def study(self):
        print("人学习")

class Student(Person):

    def __init__(self,id):
        # super(Student, self).__init__(name,age)
        Person.__init__(self)
        self.id=id
        print("儿子")
s1=Student(1001)
s1.age=10
s1.name="aaa"
print(s1.name,s1.age)
'''



#多态：前提必须要多重继承，多重继承的子类拥有相同父类属性才能实现多态
# 给人写一个功能为喂动物类，狗和猫属于动物类，然后人每次喂动物时只需要传入动物的子类就能实现喂动物
class animal(object):
    def __init__(self,name,food):
        self.name=name
        self.food=food
    def eat(self):
        print(('%s'%self.name)+'吃'+('%s'%self.food))
class dog(animal):
    def __init__(self,name,food):
        super(dog, self).__init__(name,food)
class cat(animal):
    def __init__(self,name,food):
        super(cat, self).__init__(name,food)
class person(object):
    def feed(self,animal):
        print('给%s食物'%animal.name)
        animal.eat()
class chicken(animal):
    def __init__(self):
        self.name='唧唧'
        self.food='虫子'

dog1=dog('汪汪','骨头')
cat1=cat('喵喵','鱼儿')
chicken1=chicken()
p1=person()
p1.feed(dog1)
p1.feed(cat1)
p1.feed(chicken1)



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




#多态：前提必须要多重继承，多重继承的子类拥有相同父类属性才能实现多态
# 给人写一个功能为喂动物类，狗和猫属于动物类，然后人每次喂动物时只需要传入动物的子类就能实现喂动物
class animal(object):
    def __init__(self,name,food):
        self.name=name
        self.food=food
    def eat(self):
        print(('%s'%self.name)+'吃'+('%s'%self.food))
class dog(animal):
    def __init__(self,name,food):
        super(dog, self).__init__(name,food)
class cat(animal):
    def __init__(self,name,food):
        super(cat, self).__init__(name,food)
class person(object):
    def __init__(self,name):
        self.name=name
    def feed(self,animal):
        print('%s给%s%s'%(self.name,animal.name,animal.food))
        animal.eat()
class chicken(animal):
    def __init__(self):
        self.name='长安鸡'
        self.food='虫子'
def main():
    dog1=dog('长安狗','骨头')
    cat1=cat('长安猫','鱼儿')
    chicken1=chicken()
    p1=person('刘昂')
    p1.feed(dog1)
    p1.feed(cat1)
    p1.feed(chicken1)

if __name__ == '__main__':
    main()


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



# 类的其它要点：

#1.动态添加属性和功能




#2.限制实例属性,不能动态添加
#在属性初始化前加上__slots__=元组
#元组里面放的元素才可以添加，否则不行


#3.将私有的属性变为外部可访问
# @property和@属性名.setter将私有属性分别可直接get和可改变
