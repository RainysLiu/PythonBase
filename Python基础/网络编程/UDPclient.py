'''
import socket
#UDP不需要建立与服务器的连接，但不能保证数据到达
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data=input('请输入：')
    # 发送数据:
    s.sendto(data.encode(), ('10.35.161.23', 2425))
    # 接收数据:
'''



import time
import socket
while True:
    str=input('请输入：')
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.connect(("192.168.17.1",8000))
    udp.send(('客户端：'+str).encode('gbk'))
    time.sleep(10)
    print(udp.recv(1024).decode('gbk'))
