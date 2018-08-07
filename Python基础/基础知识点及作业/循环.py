
#按要求打印‘我爱你’
'''
i=1
import time
n=10
while i<=n:
    for x in range(1,n-i+1):
        print('  ',end='')
    print('我',end='')  
    for x in range(1,i+1):
        print('爱',end='')
    print('你')
    time.sleep(0.5)
    i+=1
'''


#打印n行我爱你，爱字一行比一行多
n=10
for x in range(0,n):
    for y in range(1,n-x):
        print(' ',end='')
    print('我',end='')
    for z in range(1,x+1):
        print('爱',end='')
    print('你\n',end='')







'''
for x in  range(2):
    print(x)
    if x==1:
        break
else:
    print('wrong')
'''

#9*9乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print(('%d*%d=%d'%(x,y,x*y)),end=' ')
    print('\n',end='')


'''
#判断账户密码
account,password='1072799939','110'
a,p=str(input('请输入账户:')),str(input('请输入密码:'))
if a==account and p==password:
        print('欢迎进入%s的世界！'%account)
else:
        print('用户名或密码输入错误，请重试！')

'''


#打印倒三角星星

n=5
for x in range(1,n+1):
        for y in range(1,x+1): 
            print('*',end='')
        print('\n',end='')
for w in range(n+1,2*n):
        for q in range(1,2*n-w+1):
                print('*',end='')
        print('\n',end='')