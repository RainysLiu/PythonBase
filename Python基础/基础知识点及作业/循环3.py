'''
dao=int(input('please enter 刀长：'))
if dao>10:
    print('请下车')
else:
    print('请上车')
    
'''
'''
money=int(input('please enter money：'))
if money>2:
    print('请上车')
    zuowei=int(input('please enter seat：'))
    if zuowei>0:
        print('请坐下')
    else:
        print('没有座位了')
else:
    print('余额不足')
'''
'''
#石头剪刀布
import random
p=int(input('请出手势：剪刀（1），石头（2），布（3）：\n'))
c=random.randint(1,3)
'''

'''
if r==1:
    if p==1:
        print('平局')
    elif p==2:
        print('你赢了')
    else:
        print('你输了')
elif r==2:
    if p==1:
        print('你输了')
    elif p==2:
        print('平局')
    else:
        print('你赢了')
else:
    if p==1:
        print('你赢了')
    elif p==2:
        print('你输了')
    else:
        print('平局')
'''



'''
if ((p==1) and (c==3)) or ((p==2) and (c==1)) or ((p==3) and (c==2)):
    print('你赢了')
elif p==c:
    print('平局')
else:
   print('你输了')
print('你出的是%s,电脑出的是%s'%(p,c))
'''



##三局两胜或三局战平猜拳游戏，用一个计数器，猜谜两次时，通过计数器的值来判断是否前两次连续胜利或连续失败，如果是，终止猜谜游戏
##猜谜三次时，通过计数器可能的值的各种情况来判断最终胜负
'''
import random
def caiquan():
    p=int(input('请出手势：剪刀（1），石头（2），布（3）：\n'))
    c=random.randint(1,3)
    if ((p==1) and (c==3)) or ((p==2) and (c==1)) or ((p==3) and (c==2)):
        print('你赢了！电脑出的%d'%c)
        return 1
    elif p==c:
        print('平局！电脑出的%d'%c)
        return 0
    else:
        print('你输了！电脑出的%d'%c)
        return -1
s=0
i=0
for x in range(0,3):
    m=caiquan()
    if  m==1:
        s+=1
    elif m==-1:
        s-=1
    else:
        s+=0
    if x==1:
        if s==-2:
            print('你最终输了!')
            break
        elif s==-2:
            print('你最终赢了!')
            break
    i+=1
if i==3:
    if s==0:
        print('最终平局！')
    elif s==1 or s==2:
        print('你最终赢了！')
    elif s==-1 or s==-2:
        print('你最终输了！')
'''

#第二种方法，最终胜负通过电脑和人两个计数器的值分别为多少的各种情况来判断
'''
import random
def caiquan():
    p=int(input('请出手势：剪刀（1），石头（2），布（3）：\n'))
    c=random.randint(1,3)
    if ((p==1) and (c==3)) or ((p==2) and (c==1)) or ((p==3) and (c==2)):
        print('你赢了！电脑出的%d'%c)
        return 1
    elif p==c:
        print('平局！电脑出的%d'%c)
        return 0
    else:
        print('你输了！电脑出的%d'%c)
        return -1
s,w=0,0
i=0
for x in range(0,3):
    m=caiquan()
    if  m==1:
        s+=1
    elif m==-1:
        w+=1
    elif m==0:
        s+=0
        w+=0
    if x==1:
        if w==2:
            print('游戏结束！你最终输了!')
            break
        elif s==2:
            print('游戏结束！你最终赢了!')
            break
    i+=1
if i==3:
    if s==0 or (s==1 and w ==1):
        print('游戏结束！最终平局！')
    elif s==2 or (s==1 and w==0):
        print('游戏结束！你最终赢了！')
    elif w==2 or (w==1 and s==0):
        print('游戏结束！你最终输了！')
'''


#第三种方法,最终胜负判断通过比较电脑和人的计数器大小的
import random
def caiquan():
    p=int(input('请出手势：剪刀（1），石头（2），布（3）：\n'))
    c=random.randint(1,3)
    if ((p==1) and (c==3)) or ((p==2) and (c==1)) or ((p==3) and (c==2)):
        print('你赢了！电脑出的%d'%c)
        return 1
    elif p==c:
        print('平局！电脑出的%d'%c)
        return 0
    else:
        print('你输了！电脑出的%d'%c)
        return -1
s,w=0,0
i=0
for x in range(0,3):
    m=caiquan()
    if  m==1:
        s+=1
    elif m==-1:
        w+=1
    elif m==0:
        s+=0
        w+=0
    if x==1:
        if w==2:
            print('游戏结束！你最终输了!')
            break
        elif s==2:
            print('游戏结束！你最终赢了!')
            break
    i+=1
if i==3:
    if s==w:
        print('游戏结束！最终平局！')
    elif s>w:
        print('游戏结束！你最终赢了！')
    elif s<w:
        print('游戏结束！你最终输了！')

    
        
        
        
        
        
    


        
