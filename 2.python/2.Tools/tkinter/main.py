#!/bin/python3
#########################################################################
# File Name: main.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Fri Mar 15 16:58:20 2024
#########################################################################

# reference: https://likegeeks.com/python-gui-examples-tkinter-tutorial/

# Python2.x 导入方法
# from Tkinter import *
# Python3.x 导入方法
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import threading

def mThread(func,  *args):
    mthd = threading.Thread(target=func, args=args)
    # 主线程退出就直接让子线程跟随退出,不论是否运行完成。
    mthd.setDaemon(True)
    mthd.start()


# Listbox
def mListbox(fatherWin, locR, locC):
    li     = ['C','python','php','html','SQL','java']
    # create Listbox
    listb  = tk.Listbox(fatherWin)
    # insert data
    for item in li:
        listb.insert(0,item)
    listb.grid(row = locR, column = locC)
    # listb.pack()


def mLabel(fatherWin, locR, locC):
    num=0
    lbl = tk.Label(fatherWin, text="mLabel", font=("Arial Bold", 50))
    # set loc
    lbl.grid(row = locR, column = locC)


# Button
def mBtnClicked(msg):
    print("button is clicked msg:{}".format(msg))

def mButton(fatherWin, locR, locC):
    # lambda syntax:
    # lambda arguments: expression
    para = "click test"
    # command 没有参数，因此labbda表达式也不能带参数
    btn = tk.Button(fatherWin, text="Click Me", bg="orange", fg="red",
                 command=(lambda : mThread(mBtnClicked, para)))
    btn.grid(row = locR, column = locC)


# Entry
def entryAction(txt):
    print("txt:{}".format(txt.get()))

def mEntry(fatherWin, locR, locC):
    txt = tk.Entry(fatherWin,width=10)
    txt.grid(row = locR, column = locC)
    # txt.bind('<Enter>', lambda event : print("x:{} y:{}".format(event.x, event.y)))
    txt.bind('<Return>', lambda event : mThread(entryAction, txt))
    # 设置txt为当前焦点
    txt.focus()


# Combobox
def mCombox(fatherWin, locR, locC):
    combo = ttk.Combobox(fatherWin)
    combo['values']= (1, 2, 3, 4, 5, "Text")
    combo.current(1) #set the selected item
    combo.grid(row = locR, column = locC)
    combobox1 = tk. ttk.Combobox(fatherWin, values=["Option A", "Option B"])
    # combobox1.pack()
    combobox1.grid(row = locR, column = (locC+1))
    combobox2 = tk. ttk.Combobox(fatherWin, values=["Choice 1", "Choice 2"])
    # combobox2.pack()
    combobox2.grid(row = locR, column = (locC+2))

# message box
def msgClicked():
    messagebox.showinfo('Message title', 'Message content')

def mMesgBox(fatherWin, locR, locC):
    btn = tk.Button(fatherWin, text='msg box', command=msgClicked)
    btn.grid(row = locR, column = locC)


# menu bar
def mMenuBar(fatherWin):
    menu = tk.Menu(fatherWin)
    new_item = tk.Menu(menu)
    new_item.add_command(label='New')
    new_item.add_separator()
    new_item.add_command(label='Edit')
    menu.add_cascade(label='File', menu=new_item)
    fatherWin.config(menu=menu)


def main():
    # create window
    rootWin = tk.Tk()
    rootWin.title("Welcome to tkinter")

    mListbox(rootWin, 0, 0)
    mLabel(rootWin, 0, 1)
    mButton(rootWin, 0, 2)
    mEntry(rootWin, 0, 3)
    mCombox(rootWin, 1, 0)
    mMesgBox(rootWin, 2, 0)
    mMenuBar(rootWin)

    # window size
    # rootWin.geometry('350x200')
    # ennter message loop
    rootWin.mainloop()



if __name__ == "__main__":
    main()
