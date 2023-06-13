from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='บัญชีบันทึกคนยืมเงิน',font=('AngsanaNew',36),fg='green')
L1.place(x=170,y=20)
####################################
def Button2():
    text = 'มีเยอะไม่หนีไม่จ่าย'
    messagebox.showinfo('ไม่คืนเว้ย',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=150,y=150)
B2 = ttk.Button(FB1,text='ไอ้',command=Button2) #นี่คือปุ่มของโปรแรกม
B2.pack(ipadx=20,ipady=20)
#####################################
def Button3():
    text = 'ไม่มีไม่หนีไม่จ่าย'
    messagebox.showwarning('ไม่คืนเว้ย',text)

FB2 = Frame(GUI) 
FB2.place(x=450,y=150)
B3 = ttk.Button(FB2,text='ควย',command=Button3)
B3.pack(ipadx=20,ipady=20)
#####################################
def Button4():
    text = 'เราเคยยืมเงินกันหรอ'
    messagebox.showerror('ไม่คืนเว้ย',text)

FB3 = Frame(GUI) 
FB3.place(x=300,y=150)
B4 = ttk.Button(FB3,text='หัว',command=Button4)
B4.pack(ipadx=20,ipady=20)


GUI.mainloop()
