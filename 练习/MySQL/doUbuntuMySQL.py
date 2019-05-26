#远程连接并操作Linux下MySQL数据库
import mysql.connector
# change root password to yours:
conn = mysql.connector.connect(host='10.35.165.252',user='root', password='4801',database='rainys')

cursor = conn.cursor()
#创建表:

try:
 cursor.execute('create table player (id int primary key auto_increment, name varchar(20),work varchar(10),era varchar(10))')
except:
 print('该表已存在！')
#插入记录，注意MySQL的占位符是%s:
while True:
 n=input('请输入要添加的姓名:')
 w=input('请输入该玩家职业:')
 e=input('请输入该玩家年代:')
 cursor.execute('insert into player (name,work,era) values (%s, %s,%s)', [n, w,e])
 c=input('添加成功！继续请按1 结束请按2：')
 if c=='1':
  pass
 elif c=='2':
  print('添加结束！')
  break
#更改信息
#cursor.execute("update user set name='李华' where id='%s'" % ('3'))
#删除信息
#cursor.execute("delete from user where id='%s'" % ('5'))
#提交事务:
conn.commit()
cursor.close()
'''
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from player')
values = cursor.fetchall()
print('-----------------------------------\n'
      '当前player表数据为:')
for x in values:
 print(x)
#关闭Cursor和Connection:
cursor.close()
conn.close()
'''

