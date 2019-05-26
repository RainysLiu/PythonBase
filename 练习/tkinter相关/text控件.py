import tkinter
#創建窗口
win = tkinter.Tk()
win.title('漢字成語')
win.geometry('200x200+200+200')



S='''
百里挑一、金玉满堂、
背水一战、霸王别姬、
天上人间、不吐不快、
海阔天空、情非得已、
满腹经纶、兵临城下、
春暖花开、插翅难逃、
黄道吉日、天下无双、
偷天换日、两小无猜、
卧虎藏龙、珠光宝气、
簪缨世族、花花公子、
绘声绘影、国色天香、
相亲相爱、八仙过海、
金玉良缘、掌上明珠、
'''



#创建滚动条
scroll = tkinter.Scrollbar()
#文本控件，用于显示多行文本
#此 height表示显示行数
text=tkinter.Text(win,width=30,height=5)
#将字符串插入这个text
text.insert(tkinter.INSERT,S)
#side：放到窗体的哪一边，fill填充
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.X)
#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)



#循環窗口放到最後
win.mainloop()