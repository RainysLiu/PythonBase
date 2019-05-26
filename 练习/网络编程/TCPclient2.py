import socket
import _multibytecodec
#创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('10.35.161.35', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

while True:
    data = input('请输入：')
    if data == 'exit':
        s.send(('exit').encode('utf-8'))
        s.close()
        break
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
