import pymysql
db=pymysql.connect(host="192.168.191.128",user="root",password="15191545668",database="test")

cur=db.cursor()

sql="select * from student"

try:
    cur.execute(sql)     #执行sql语句
    results = cur.fetchall()    #获取查询的所有记录
    print("id","name","time","add")
    #遍历结果
    for row in results :
        id = row[0]
        name = row[1]
        time = row[2]
        add=row[3]
        print(id,name,time,add)
except Exception as e:
    raise e
finally:
    db.close()    #关闭连接
