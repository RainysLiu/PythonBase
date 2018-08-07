#远程连接并操作win下的MySQL数据库
import mysql.connector
# change root password to yours:
conn = mysql.connector.connect(user='root', password='4801', database='rainys')
cursor = conn.cursor()
#创建表:
# try:
#  cursor.execute('create table  account (accid int primary key,name varchar(10) not null,balance int not null)')
# except:
#  print('该表已存在！')


#插入记录，注意MySQL的占位符是%s:
#cursor.execute('insert into account values(1001,"tom",500),(1002,"jerry",800),(1003,"jack",800)')
# while True:
#  n1=input('请输入你的姓名:')
#  n2= input('请输入你要转账的姓名:')
#  m=int(input('请输入你要转账的额度:'))
#  cursor.execute('update account set balance=balance-%d where name=%s ',[m, n1])
#  cursor.execute('update account set balance=balance+%d where name=%s',[m, n2])

try:
 cursor.execute('start transaction;')
 cursor.execute('update account set balance=balance-200 where name="tom"')
 cursor.execute('update account set balance=balance+200 where name="jerry"')
 conn.commit()
 print('转账成功！')
except:
 cursor.execute('rollback')
 print("系统发生异常，转账失败!")
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from account')
values = cursor.fetchall()
print('-----------------------------------\n'
      '当前账户表数据为:')
for x in values:
 print(x)
#关闭Cursor和Connection:
cursor.close()
conn.close()