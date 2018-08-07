class admin(object):
    def __init__(self,account,password):
        self.account=account
        self.password=password
    def login(self):
        i=0
        while True:
            print('*********xxx银行ATM系统管理界面*********')
            c=input('---登入系统请按1---\n---退出程序请按2---\n***************************************\n')
            if c=='1':
                a=input('请输入管理员账户:')
                p=input('请输入管理员密码：')
                if a==self.account and p==self.password:
                    print('登陆成功！')
                    return 'ok'
                    break
                else:
                    i+=1
                    if i==3:
                        print('连续输错三次，自动退出程序!')
                        return 'exit'
                        break
                    print('用户名或密码输入错误！请重输：')
            if c=='2':
                return 'exit'
                break

    def choiceUI(self):
        print('''
************欢迎来到xxx银行ATM系統***************
*****************功能选择页**********************
**   1. 开户        2. 查询        3. 存款     **
**   4. 取款        5. 转账        6. 改密     ** 
**   7. 锁定        8. 解锁        9. 销户     **
************************************************
**************(退出至管理員頁面请按Q)*************''')
if __name__=='__main__':
    adm1=admin('ADMIN','123')
    # adm1.login()
    adm1.choiceUI()