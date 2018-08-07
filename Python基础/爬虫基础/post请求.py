import urllib.request
import urllib.parse
url = 'http://www.sunck.wang:8085/from'
#字典的键值一般为input标签的name属性的值
data={
    'user':'sunck',
    'password':'666'
}
#对要发送的数据进行打包
postdata=urllib.parse.urlencode(data).encode('utf-8')
#请求体
req=urllib.request.Request(url,data=postdata)

req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/66.0.3359.139 Safari/537.36')
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
