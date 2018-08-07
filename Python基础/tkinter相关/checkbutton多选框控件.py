import tkinter
#創建窗口
win = tkinter.Tk()
win.title('tkinter')
win.geometry('200x200+200+200')


def updata():
    message=''
    if like1.get()==True:
        message+='money\n'
    if like2.get()==True:
        message+='power\n'
    if like3.get()==True:
        message+='love\n'
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)



#要绑定的变量
like1=tkinter.BooleanVar()
#创建多选框
check1=tkinter.Checkbutton(win,text='money',variable=like1,command=updata)
check1.pack()
like2=tkinter.BooleanVar()
check2=tkinter.Checkbutton(win,text='power',variable=like2,command=updata)
check2.pack()
like3=tkinter.BooleanVar()
check3=tkinter.Checkbutton(win,text='love',variable=like3,command=updata)
check3.pack()
text = tkinter.Text(win, width=50, height=5,)
text.pack()





#循環窗口放到最後
win.mainloop()