from io import StringIO
import os
import pickle

s=StringIO()
s.write('贺磊磊')
s.write('是帅逼')
#用指針讀取
s.seek(0,0)
print(s.read())
#用getvalue取值
print(s.getvalue())
#文件讀寫
with open(os.path.join(os.getcwd(), 'hll.txt'),'a') as f:
    f.write(s.getvalue())
#序列化和反序列化
#序列化
dic={'1':'華爲','2':'百度','3':'阿里巴巴'}
with open(os.path.join(os.getcwd(), 'xueliehua.txt'),'wb') as f:
    pickle.dump(dic,f)
#直接讀取只能顯示二進制
with open(os.path.join(os.getcwd(), 'xueliehua.txt'),'rb') as f:
    print(f.read())
#用pickle.load讀取二進制
with open(os.path.join(os.getcwd(), 'xueliehua.txt'),'rb') as f:
    print(pickle.load(f))

#將一個類序列化存入文件后讀取

#1.普通方法將類序列化后存入文件
class cat(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
cat01=cat('長安貓','99')
with open(os.path.join(os.getcwd(), 'cat01.txt'),'wb') as f:
    pickle.dump(cat01, f)
with open(os.path.join(os.getcwd(), 'cat01.txt'),'rb') as f:
    c1=pickle.load(f)
    print(c1)
    print('名字:'+c1.name,'年齡:'+c1.age)


#利用json進行序列化和反序列化,需要通過字典
#2.將實例轉化爲字典，再將字典轉化爲json序列化
import json
cat02=cat('小可愛','15')
json02=json.dumps(cat02,default=lambda object:object.__dict__)    #轉化爲字典后json序列化
with open(os.path.join(os.getcwd(), 'cat02.json'),'wb') as f:
    pickle.dump(json02, f)
def dic2cat(jsonobject):
    return cat(jsonobject['name'],jsonobject['age'])
with open(os.path.join(os.getcwd(), 'cat02.json'),'rb') as f:
    c2=json.loads(pickle.load(f),object_hook=dic2cat)
    print('名字:'+c2.name,'年齡:'+c2.age)
