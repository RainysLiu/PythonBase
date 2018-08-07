import tkinter
#創建窗口
win = tkinter.Tk()
win.title('漢字成語')
win.geometry('400x400+200+200')
#標簽框架
label=tkinter.Label(win,text='錦囊妙計\n千鈞一髮',bg='yellow',fg='blue',font=('楷体',30),width=20,height=5,anchor='s')
label.pack()


#enter框架
entry=tkinter.Entry(win)
entry.pack()
#按钮框架
button=tkinter.Button(win,text='打印',anchor='s',command=lambda: print(entry.get()))
button.pack()


#循環窗口放到最後
win.mainloop()