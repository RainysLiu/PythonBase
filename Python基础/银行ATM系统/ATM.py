from card import card
from user import user
import random
class ATM(object):
    def __init__(self,userlist):
        self.userlist=userlist
    #建户
    def creataccount(self):
        n=input('请输入姓名：')
        id=input('请输入身份证号：')
        tel=input('请输入手机号：')
        ICcradnumber=(''.join(random.sample('0123456789',6)))
        while True:
            p1=input('请设置密码：')
            p2=input('请再次设置密码：')
            if p1==p2:
                print('密码设置成功！')
                break
            else:
                print('两次输入密码不一致,请重新设置！')
        while True:
            b=int(input('请充值金额，至少10元：'))
            if b>=10:
                print('建卡成功，账户为%s，当前余额为%d元！'%(ICcradnumber,b))
                break
            else:
                print('充值金额小于十元，请重新充值！')
        card1=card(ICcradnumber,p2,b,'unlock')
        user1=user(n,tel,id,card1)
        (self.userlist)[ICcradnumber]=user1
    #查询
    def serach(self):
        a=input('请输入要查询的账户：')
        if a in self.userlist:
            if self.userlist[a].card.state == 'unlock':
                i=0
                while True:
                    p=input('请输入密码：')
                    if p==self.userlist[a].card.password:
                        print('客户%s**你好，你的账户%s余额为%d元！'%(self.userlist[a].name[0],a,self.userlist[a].card.balance))
                        break
                    else:
                        print('密码输入错误,请重输！')
                        i+=1
                        if i==3:
                            self.userlist[a].card.state = 'lock'
                            print('密码连续三次输错 ，账户已自动锁定！')
                            break
            else:
                print('该账户已被锁定！')
        else:
            print('账户不存在！')
    def savemoney(self):
        a = input('请输入要存款的账户：')
        if a in self.userlist:
            if self.userlist[a].card.state == 'unlock':
                print('你要存入的账户信息如下:\n账户：%s 户主：%s**\n确认存钱请按1 放弃请按任意键'%(a,self.userlist[a].name[0]))
                c=input()
                if c=='1':
                    while True:
                        money = int(input('请输入要存的钱数：'))
                        self.userlist[a].card.balance += money
                        print('存款成功，你当前账户%s余额为%d元！' % (a, self.userlist[a].card.balance))
                        m=input('继续存款请按1，结束存款请按任意键...')
                        if m==1:
                            pass
                        else:
                            break
                else:
                    print('你已放弃存款！')
            else:
                print('该账户已锁定！')
        else:
            print('账户不存在！')
    def reducemoney(self):
        a = input('请输入要取钱的账户：')
        if a in self.userlist:
            if self.userlist[a].card.state == 'unlock':
                for i in range(3):
                    p = input('请输入密码：')
                    if p == self.userlist[a].card.password:
                        money = int(input('请输入要取的钱数:'))
                        if money<=self.userlist[a].card.balance:
                            self.userlist[a].card.balance -=money
                            print('取款成功，当前账户%s余额为%d元！' % (a, self.userlist[a].card.balance))
                            break
                        else:
                            print('无法取款，账户余额不足！')
                            break
                    else:
                        print('密码输入错误,请重输！')
                else:
                    self.userlist[a].card.state = 'lock'
                    print('密码连续三次输错 ，账户已自动锁定！')
            else:
                print('该账户已锁定！')
        else:
            print('账户不存在！')
    def transfer(self):
        a = input('请输入你的账户：')
        if a in self.userlist:
            if self.userlist[a].card.state == 'unlock':
                i=0
                while True:
                    p = input('请输入密码：')
                    if p == self.userlist[a].card.password:
                        a2 = input('请输入要转账的账户：')
                        if a2 in self.userlist:
                            print('你要转账的账户信息如下:\n账户：%s 户主：%s**\n确认转账请按1 放弃请按任意' % (a2, self.userlist[a2].name[0]))
                            c = input()
                            if c == '1':
                                money = int(input('请输入要转入的钱数：'))
                                if money <= self.userlist[a].card.balance:
                                    self.userlist[a].card.balance -= money
                                    self.userlist[a2].card.balance += money
                                    print('转账成功，您当前账户%s余额为%d元' % (a, self.userlist[a].card.balance))
                                    break
                                else:
                                    print('无法转账，账户余额不足！')
                                    break
                            else:
                                print('你已放弃转账！')
                                break
                        else:
                            print('要转入的账户不存在！')
                            break
                    else:
                        print('密码输入错误,请重输！')
                        i+=1
                        if i==3:
                            self.userlist[a].card.state = 'lock'
                            print('密码连续三次输错 ，账户已自动锁定！')
                            break
            else:
                print('该账户已锁定！')
        else:
            print('账户不存在！')
    def changepassword(self):
        a = input('请输入要改密的账户：')
        if a in self.userlist:
            if self.userlist[a].card.state == 'unlock':
                i=0
                while True:
                    p = input('请输入密码：')
                    if p == self.userlist[a].card.password:
                        NewPassword=input('请输入新密码：')
                        self.userlist[a].card.password=NewPassword
                        print('账户%s密码修改成功！'%a)
                        break
                    else:
                        print('密码输入错误,请重输！')
                        i += 1
                        if i == 3:
                            self.userlist[a].card.state = 'lock'
                            print('密码连续三次输错 ，账户已自动锁定！')
                            break
            else:
                print('该账户已锁定！')
        else:
                print('账户不存在！')

    def lock(self):
        a = input('请输入要锁定的账户：')
        if a in self.userlist:
            if self.userlist[a].card.state == 'unlock':
                i=0
                for x in range(3):
                    p = input('请输入密码：')
                    if p == self.userlist[a].card.password:
                        self.userlist[a].card.state='lock'
                        print('账户%s锁定成功！'%a)
                        break
                    else:
                        print('密码输入错误！')
                else:
                    self.userlist[a].card.state = 'lock'
                    print('密码连续三次输错 ，账户已自动锁定！')
            else:
                print('该账户已经处于锁定状态！')
        else:
            print('账户不存在！')

    def unlock(self):
        a = input('请输入要解锁的账户：')
        if a in self.userlist:
            if self.userlist[a].card.state == 'lock':
                i=0
                while True:
                    p = input('请输入密码：')
                    if p == self.userlist[a].card.password:
                        self.userlist[a].card.state='unlock'
                        print('账户%s解锁成功！'%a)
                        break
                    else:
                        print('密码输入错误,请重输！')
                        i += 1
                        if i == 3:
                            self.userlist[a].card.state = 'lock'
                            print('密码连续三次输错 ，账户已自动锁定！')
                            break
            else:
                print('该账户未锁定，无需解锁！')
        else:
            print('账户不存在！')

    def deleteAccount(self):
        a = input('请输入要注销的账户:')
        if a in self.userlist:
            if self.userlist[a].card.state == 'lock':
                i=0
                while True:
                    p = input('请输入密码：')
                    if p == self.userlist[a].card.password:
                        self.userlist.pop(a)
                        print('账户%s注销成功！'%a)
                        break
                    else:
                        print('密码输入错误！请重输！')
                        if i == 3:
                            self.userlist[a].card.state = 'lock'
                            print('密码连续三次输错 ，账户已自动锁定！')
                            break
            else:
                print('该账户已锁定！')
        else:
            print('账户不存在！')
if __name__=='__main__':
    ATM1=ATM({})
    ATM1.creataccount()
    ATM1.serach()
    ATM1.savemoney()
    ATM1.reducemoney()
    ATM1.changepassword()
