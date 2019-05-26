import tkinter
#創建窗口
win = tkinter.Tk()
win.title('漢字成語')
win.geometry('400x400+200+200')

#標簽框架
label=tkinter.Label(win,text='錦囊妙計\n千鈞一髮',bg='yellow',fg='blue',font=('楷体',30),width=20,height=5,anchor='s')
label.pack()
#按钮框架
button=tkinter.Button(win,text='退出',anchor='s',command=win.quit)
button.pack()


#enter框架

#设置变量
v=tkinter.Variable()
#设定输入的内容
v.set('大驾光临')
entry=tkinter.Entry(win,show='*',textvariable=v)
#打印输入框變量的值
print(v.get())
print(entry.get())
#執行輸入功能
entry.pack()






#循環窗口放到最後
win.mainloop()