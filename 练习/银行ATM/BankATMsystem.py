import os
import pickle
import time
from user import user
from card import card
from ATM import ATM
from admin import admin
def ATMsystem():
    while True:
        admin1 = admin('ADMIN', '123')
        m=admin1.login()
        if m=='ok':
            filepath = os.path.join(os.getcwd(), 'AllUserlist.txt')
            f = open(filepath, 'rb')
            Userlist = pickle.load(f)
            f.close()
            ATM1 = ATM(Userlist)
            print('ATM系统当前账户有：')
            print([x for x in ATM1.userlist])
            print('正在进入ATM系统界面！请稍候...')
            time.sleep(2)
            while True:
                admin1.choiceUI()
                c=input('请输入功能选项：')
                if c=='1':      #建户
                    ATM1.creataccount()
                    time.sleep(2)
                elif c=='2':
                    ATM1.serach()
                    time.sleep(2)
                elif c=='3':
                    ATM1.savemoney()
                    time.sleep(2)
                elif c=='4':
                    ATM1.reducemoney()
                    time.sleep(2)
                elif c=='5':
                    ATM1.transfer()
                    time.sleep(2)
                elif c=='6':
                    ATM1.changepassword()
                    time.sleep(2)
                elif c=='7':
                    ATM1.lock()
                    time.sleep(2)
                elif c=='8':
                    ATM1.unlock()
                    time.sleep(2)
                elif c=='9':
                    ATM1.deleteAccount()
                    time.sleep(2)
                elif c=='Q':
                    filepath = os.path.join(os.getcwd(), 'AllUserlist.txt')
                    f = open(filepath, 'wb')
                    pickle.dump(ATM1.userlist, f)
                    f.close()
                    print('正在保存用户信息并退出！请稍候...')
                    time.sleep(1)
                    print('退出至管理员登录界面成功！')
                    break
                else:
                    print('输入有误，请重新输入！')
                    time.sleep(1)
        if m=='exit':
            print('正在退出程序！请稍候...')
            time.sleep(2)
            break
ATMsystem()
