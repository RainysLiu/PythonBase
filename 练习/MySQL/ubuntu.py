import pymysql
conn = pymysql.Connect(
    host='10.35.165.219',
    port=3306,
    user='root',
    passwd='4801',
    db="rainys",
    charset='utf8'
)
cursor=conn.cursor()
sql="insert into student(name,sex,score,stuid)values('%s','%s',%.1f,%d)"
data=('祝枝山',"女",96.5,3)
cursor.execute(sql%data)
conn.commit()
print("执行成功")
cursor.close()
conn.close()


