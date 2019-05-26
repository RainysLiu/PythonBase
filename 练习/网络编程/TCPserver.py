import socket
import time
import threading
#创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#创建一个监听端口:127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，
# 也就是说，外部的计算机无法连接进来。
s.bind(('10.35.161.35', 9999))
#调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('等待连接...')


#创建一个线程或进程来处理
# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
    print('接受了一个新连接来自 %s:%s...' % addr)
    sock.send(('欢迎訪問服務器!').encode('utf-8'))
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            print('连接 %s:%s已被客戶端关闭.' % addr)
            sock.close()
            break
        print('來自客戶端：'+data.decode('utf-8'))
        sock.send(('服務器：好的，我收到了！%s!'%data.decode('utf-8')).encode('utf-8'))


#通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



