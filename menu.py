from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime
from database import *
from logfile import *


# ----------------------global variables-----------------------

b1,b2,b3,b4,cur,con,e1,e2,e3,e4,e5,i,ps=None,None,None,None,None,None,None,None,None,None,None,None,None
window,win=None,None
com1d,com1m,com1y,com2d,com2m,com2y=None,None,None,None,None,None

month=['January','February','March','April','May','June','July','August','September','October','November','December']
y = list(range(2020, 2040))
d = list(range(1,32))


# --------------------------Main Window-------------------------

def libr():
    global window
    global win,b1,b2,b3,b4
    win=Tk()
    win.title('Library')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    b2=Button(win, height=2,width=25,text=' Issue Book ',command=issuebook)
    b3=Button(win, height=2,width=25,text=' Return Book ',command=returnbook)
    b4=Button(win, height=2,width=25,text=' View Books ',command=viewbook)

    b2.place(x=110,y=80)
    b3.place(x=110,y=130)
    b4.place(x=110,y=180)
    win.mainloop()


# --------------------------Issue Book Window------------------------------

def issuebook():
    global win
    win.destroy()
    win=Tk()
    win.title('Issue Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    name=Label(win,text='ISSUE ',font='Helvetica 30 bold')
    branch=Label(win,text='BOOK',font='Helvetica 30 bold')

    sid=Label(win,text='Member ID',)
    no=Label(win,text='BOOK ID')
    issue=Label(win,text='ISSUE DATE')
    global e1,b,b1
    e1=Entry(win,width=25)
    global e4
    e4=Entry(win,width=25)
    global com1y,com1m,com1d,com2y,com2m,com2d
    com1y=Combobox(win,value=y,width=5)
    com1m=Combobox(win,value=month,width=5)
    com1d=Combobox(win,value=d,width=5)

    now=datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)
    
    b=Button(win, height=2,width=21,text=' ISSUE BOOK ',command=lambda:messagebox.showinfo(title="Info",message=bookcheckout(e1.get(),e4.get(),com1d.get()+"/"+com1m.get()+"/"+com1y.get(),"database.txt",'r')))
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=closebooks)
    name.place(x=55,y=30)
    branch.place(x=225,y=30)
    sid.place(x=70,y=130)
    no.place(x=70,y=170)
    issue.place(x=70,y=210)
    e1.place(x=180,y=130)
    e4.place(x=180,y=170)
    com1y.place(x=180,y=210)
    com1m.place(x=230,y=210)
    com1d.place(x=280,y=210)

    b.place(x=178,y=270)
    b1.place(x=178,y=312)
    win.mainloop()



# ----------------------------------Closing Function-----------------------------
def closebooks():
    global win
    win.destroy()
    libr()


# -----------------------------------Return Book Window-------------------------

def returnbook():
    global win
    win.destroy()
    win=Tk()
    win.title('Return Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    ret=Label(win,text='RETURN ',font='Helvetica 30 bold')
    book=Label(win,text='BOOK',font='Helvetica 30 bold')
    no=Label(win,text='BOOK ID')
    issue=Label(win,text='ISSUE DATE')
    date=Label(win,text='RETURN DATE')
    exp=Label(win,text='')
    global b,b1
    global e4
    e4=Entry(win,width=25)
    global com1y,com1m,com1d,com2y,com2m,com2d
    com1y=Combobox(win,value=y,width=5)
    com1m=Combobox(win,value=month,width=5)
    com1d=Combobox(win,value=d,width=5)
    com2y=Combobox(win,value=y,width=5)
    com2m=Combobox(win,value=month,width=5)
    com2d=Combobox(win,value=d,width=5)
    now=datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)

    b=Button(win, height=2,width=21,text=' RETURN BOOK ',command=lambda : messagebox.showinfo("Info",message=bookreturn(e4.get(),com2d.get()+"/"+com2m.get()+"/"+com2y.get(),com1d.get()+"/"+com1m.get()+"/"+com1y.get(),'database.txt','r')))
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=closebooks)
    ret.place(x=55,y=30)
    book.place(x=225,y=30)
    no.place(x=70,y=120)
    issue.place(x=80,y=210)
    date.place(x=70,y=160)
    exp.place(x=70,y=200)
    e4.place(x=180,y=120)
    com1y.place(x=180,y=160)
    com1m.place(x=230,y=160)
    com1d.place(x=280,y=160)
    com2y.place(x=180,y=210)
    com2m.place(x=230,y=210)
    com2d.place(x=280,y=210)
    b.place(x=178,y=270)
    b1.place(x=178,y=312)
    win.mainloop()


# --------------------------------Search Book Window----------------------------

#function to make table in search window
def treeviews(details):
    treeview=Treeview(win,columns=("ID","Title","Author","Member_ID"),show='headings')
    treeview.heading("ID", text="ID")
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Member_ID", text="Member_ID")
    treeview.column("ID", anchor='center')
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Member_ID", anchor='center')
    index=0
    iid=0
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    

# function for searching book

def viewbook():
    global win
    win.destroy()
    win=Tk()
    win.title('View Books')
    win.geometry("800x300+270+180")
    win.resizable(False,False)
    global b1,b,e1

    no=Label(win,text='BOOK Title') 
    e1=Entry(win,width=25)
    b=Button(win, height=2,width=21,text=' Search ',command=lambda : treeviews(booksearch(e1.get())) )
    b1=Button(win, height=2,width=21,text=' CLOSE ',command=closebooks)
    no.place(x=50,y=240)
    e1.place(x=120,y=240)
    b.place(x=300,y=240)
    b1.place(x=550,y=240)

    win.mainloop()



if __name__ == "__main__":
    libr()