import urllib.request
import os
#项服务器请求访问，返回一个网页的源码文件
response=urllib.request.urlopen('http://www.baidu.com')
# #读取
# data=response.read()
# print(type(data))
# #将网页源码写入文件
# with open(os.path.join(os.getcwd(),'baidu.html'),'wb') as f:
#     f.write(data)
'''
#读取文件所有内容，并且返回一个列表,每个元素都是bytes，需要转换为utf-8字符串
codelist=response.readlines()
for x in codelist:
    str=x.decode('utf-8')
    print(str)
'''

#response属性
print(response.info())   #返回当前环境的所有信息

s=response.getcode()        #返回狀態
if s==200 or s==304:
    print('獲取成功')

#爬取的内容直接写入文件
urllib.request.urlretrieve('http://www.baidu.com',
                           filename='F:\Rainy\workspace\Python基础\爬虫\\baidu1.html'
                           )
