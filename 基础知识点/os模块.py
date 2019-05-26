# #os模块
# import os
#
# # 获取当前文件路径
# print(os.getcwd())
# #获取所有文件夹
# path='C:\\Users\Rainy\Desktop\est'
# print(os.listdir(path))
#
# #创建多层文件夹
# #os.makedirs('C:\\Users\Rainy\Desktop\est\ee\ee\ee\ee\ee')
#
# #删除
# #os.rmdir('C:\\Users\Rainy\Desktop\est\ee\ee\ee\ee')
#
# #文件改名
#
# #os.rename('10.txt','es.txt')
#
# #相对路径转绝对路径
# print(os.path.abspath(path))
#
# #将文件名和路径拆分
# path='C:\\Users\Rainy\Desktop\est\\10.txt'
# print(os.path.split(path))
# #将文件名和路径拼接
# path='C:\\Users\Rainy\Desktop\est\\10.txt'
# print(os.path.join(path))
# #获得后缀
# path='C:\\Users\Rainy\Desktop\est\\10.txt'
# print(os.path.splitext(path))
#
# #获取文件大小
# path='C:\\Users\Rainy\Desktop\est\\10.txt'
# print(os.path.getsize(path))



# import os
# def wenjian(path):
#     s=os.listdir(path)
#     for x in s:
#         path2=os.path.join(path,x)
#         if os.path.isfile(path2):
#             print('是文件',x)
#         else:
#             print('是目录',x)
#             wenjian(path2)
# wenjian('C:\\Users\Rainy\Desktop\est')






# s2=os.listdir(path)
# print(s2)
# for x in range(len(s2)):
#     if '.' not in s2[x]:
#         path='C:\\Users\Rainy\Desktop\est'+'\\'+s[x]+'\\'+s[x]
#         s3=os.listdir(path)
#         print(s3)

#自定义模块导入
import HLLS.Hll
if __name__=='__main__':
    HLLS.Hll.du()

#导入内部库
# import time
# #世界戳
# c1=time.time()
# print('%f'%c1)
# #世界标准时间,存于元组
# c2=time.gmtime(c1)
# print(c2)
# #本地时间，存于元组
# c3=time.localtime(c1)
# print(c3)
# #将元组转为时间戳
# print(time.mktime(c3))
# #将时间元组转换为字符串
# print(time.asctime(c3))
# #将时间戳转换为字符串
# print(time.ctime(c1))
# #将时间转换为特定格式字符串
# # while True:
# strt=time.strftime('%Y-%m-%d %H:%M:%S')
# print(strt)
#     # print(strt)
#     # time.sleep(1)

# #将指定的时间字符串转换为元组
# tuplet=time.strptime(strt,'%Y-%m-%d %H:%M:%S')
# print(tuplet)
# #测试运行时间
# sum=0
# i=0
# while i<=1000000:
#     sum+=i
#     i+=1
# print(sum)
# print(time.clock())
#
#
#
# #日历模块
# import calendar
# print(calendar.month(2018,6))
# print(calendar.calendar(2018))
# #判断是否为闰年
# print(calendar.isleap(2018))
# #获取指定月份的天数并判断第一天是星期几
# print(calendar.monthrange(2018,6))




