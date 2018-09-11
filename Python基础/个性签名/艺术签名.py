
from tkinter import *
from tkinter import messagebox
import requests
import re
from PIL import ImageTk

#模拟浏览器发送请求并下载返回的图片
def download():
    startUrl = 'http://www.uustv.com/'
    #通过输入框获取名字
    name = enter.get()
    if not name:
        messagebox.showinfo('提示：','输入姓名为空！')
    else:
        #post请求携带的参数
        data= {
            'word':name,
            'sizes':60,
            'fonts':'haku.ttf',
            'fontcolor':'#000000'
        }
        #通过post请求获取返回的html页面
        result = requests.post(startUrl,data = data)
        print(result.status_code)
        result.encoding='utf8'
        html = result.text
        #通过正则在返回的html页面里找返回的图片路径
        reg ='<div class="tu">.*?<img src="(.*?)"/></div>'
        imagePath = re.findall(reg,html)
        #拼接图片的完整路径
        imgUrl = startUrl + imagePath[0]
        print('临时图片路径:%s'%imgUrl)
        #获取图片内容并下载到本地
        response = requests.get(imgUrl).content
        f = open('{}.gif'.format(name), 'wb')
        f.write(response)
        #创建一个Tk兼容的照片对象
        bm = ImageTk.PhotoImage(file ='{}.gif'.format(name))
        #创建一个带有image的标签
        label2 = Label(root,image=bm)
        #image属性
        label2.bm = bm
        #把带有图片的标签放到窗口
        label2.grid(row = 2,columnspan = 4)

#主程序，实现创建窗口并展示图片


#创建窗口对象
root = Tk()
#窗口标题
root.title('艺术签名设计')
#窗口大小
root.geometry('600x300')
#窗口的初始位置
root.geometry('+400+300')
#标签的控件
label = Label(root,text = '请输入名字',font = ('微软雅黑',14),)
#将标签放在窗口
label.grid(row = 0,column = 0)
#输入框
enter = Entry(root,font = ('微软雅黑',10))
#设置输入框的位置
enter.grid(row = 0,column = 1)
#点击按钮
button = Button(root,text = '立即设计',font =('华文行楷',15),command = download) #调用下载函数
#设置点击按钮的位置
button.grid(row = 1,column = 0)
#消息循环，可以理解为显示窗口
root.mainloop()



