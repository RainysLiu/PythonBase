

'''
import re



phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)
'''


#电话号码判断
import re
def checkMobile(strData):
    CMCCRule=r"^(13[4-9]|15[0-2]|15[7-9]|18[2,3,7,8]|147)\d{8}$"
    CCrule=r"^(13[0,1,2,6]|18[5,6]|145)\d{8}$"
    Cnetrule=r"^(133|153|18[0,1,9])\d{8}$"
    rescmcc = re.findall(CMCCRule,strData)
    rescc=re.findall(CCrule,strData)
    rescnet=re.findall(Cnetrule,strData)
    if rescmcc:
        print('%s是中国移动号码'%strData)
    elif rescc:
        print('%s是中国联通号码'%strData)
    elif rescnet:
        print('%s是中国电信号码'%strData)
    else:
        print('这不是一个手机号码')
checkMobile('18392146040')



#正则表达
#match只能匹配开头
"""
import re
a=re.match(r'^\d{10}$','1203145647')
print(a)
#serach只能总开头匹配，找到一个就停止
import re
a=re.search(r'a12','mma1203145647')
print(a)
#findall找所有，将找到的内容存于列表中
import re
a=re.findall(r'^A\d{10}$','a1203145647',re.I)      #re.I代表忽略大小写
print(a)



print(re.findall(r'\d{10}','123456789'))
print(re.findall(r'[2-5]{2}','123456789'))
print(re.findall(r'[a-zA-Z]{10}','JhHjhKJhJKJjhGhjHgghJHjklJkjhKJ'))

"""