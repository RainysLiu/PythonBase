import urllib.request
import os
import random


'''
url='http://www.baidu.com'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
req=urllib.request.Request(url,headers=header)
response=urllib.request(req)
data=response.read().decode('utf-8')
print(data)
'''

#簡單反爬蟲，運用多個agent隨機訪問
url='http://www.baidu.com'
agentlist=[
'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1']
agentstr=random.choice(agentlist)
req=urllib.request.Request(url)
req.add_header('User-Agent',agentstr)
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
