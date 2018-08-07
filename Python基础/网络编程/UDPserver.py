import socket
#SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('10.35.161.35', 8000))
print('绑定于port8000...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('接收自...%s:%s:' % addr)
    print('%s'%data.decode('gbk'))
    data=input('请回复：')
    s.sendto(('服务器：%s!' % data).encode('gbk'), addr)
