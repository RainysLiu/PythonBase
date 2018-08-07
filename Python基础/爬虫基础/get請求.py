import urllib.request
url = 'http://www.sunck.wang:8085/sunck'
response=urllib.request.urlopen(url)
data=response.read().decode('utf-8')
print(data)



