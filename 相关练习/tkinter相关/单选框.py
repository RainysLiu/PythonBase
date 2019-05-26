import tkinter
#創建窗口
win = tkinter.Tk()
win.title('tkinter')
win.geometry('200x200+200+200')
def updata():
    message=''
    if r.get()=='同意':
        message+=r.get()+'\n'
    if r.get()=='不同意':
        message+=r.get()+'\n'
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)




r=tkinter.StringVar()
#创建多单选框
radoio1=tkinter.Radiobutton(win,text='1',value='同意',variable=r,command=updata)
radoio1.pack()
radoio2=tkinter.Radiobutton(win,text='2',value='不同意',variable=r,command=updata)
radoio2.pack()

text = tkinter.Text(win, width=50, height=5,)
text.pack()
#循環窗口放到最後
win.mainloop()