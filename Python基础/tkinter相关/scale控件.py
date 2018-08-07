import tkinter
#創建窗口
win = tkinter.Tk()
win.title('t')
win.geometry('400x400+200+200')


#数字条，用户可改变值
scale=tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL,length=500)
scale.pack()
def shownumber():
    print(scale.get())
tkinter.Button(win,text='当前值',command=shownumber).pack()





#循環窗口放到最後
win.mainloop()