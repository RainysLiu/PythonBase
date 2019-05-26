
import socket
#Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
# 创建一个socket: AF_INET代表IPv4协议， SOCK_STREAM代表使用TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:新浪的IP和端口
s.connect(('www.sina.com.cn', 80))

# 发送获取首页新浪数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#关闭连接：
s.close()


#拼接的收据含HTTP头和网页本身，需要进行分割，将http头打印出来，将网页存入文件sina中
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的网页数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

