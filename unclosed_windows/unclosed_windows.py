'''
Author: wsw
Time: 20210417
'''
import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
from tkinter import *
import time


def Love():   #定义点击“喜欢”时的动作
    love = Toplevel(root)
    love.geometry('300x150+240+200')
    love.title('好巧啊，我也是')
    label = Label(love, text='好巧，我也是', font=('楷体',15))
    label.pack()
    label1 = Label(love, text='留个电话可以吗', font=('楷体', 10))
    label1.pack()
    entry = Entry(love,font=('楷体', 15))
    entry.pack()
    btn = Button(love, text = '确定', width=10, height=2, command=Sure)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)
    if time.time() - start > 60:  #设定一个时间，超过多少秒以后，点击”喜欢“可关闭
        closeall()

def Sure():  #定义点击喜欢模块中确定按钮的响应
    sure = Toplevel(root)
    sure.geometry('300x150+240+200')
    sure.title('我不信')
    label = Label(sure, text='除非你现在给我打电话', font=('楷体', 15))
    label.pack()
    label = Label(sure, text='649306635', font=('楷体', 15))
    label.pack()
    btn = Button(sure, text='好的', width=10, height=2, command=clicksure)
    btn.pack()
    sure.protocol("WM_DELETE_WINDOW", closelove)



def nolove():  #定义点击“不喜欢”时的动作
    no_love = Toplevel(root)
    no_love.geometry('300x100+250+200')
    no_love.title('你肯定是骗我的')
    label = Label(no_love, text='再考虑考虑呗', font=('楷体',25))
    label.pack()
    btn = Button(no_love, text='好的', width=10, height=2, command=no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW", closenolve)

def closeroot():  #定义点击关闭窗口的动作
   messagebox.showinfo(title='警告', message='不许关闭，好好回答')
   return

def closeall():  #定义关闭所有的方法
    root.destroy()

def closelove():  #定义点击关闭喜欢时的动作
    messagebox.showinfo('不再考虑一下嘛', message='再考虑一下吧')
    return

def closenolve():
    nolove()

def clicksure():  #定义点击确定打电话时的相应
    messagebox.showinfo('哼，你又骗我', message='我还没收到电话')
    return



if __name__ == '__main__':
    start = time.time()
    root = tk.Tk()  #新建窗口
    root.title('嘘~我喜欢你呀') #窗口名字
    root.geometry('390x350+500+220')  #窗口，385x400是大小，第1个加号是距离屏幕左边的宽，第2个加号是距离屏幕顶部的高。
    root.protocol("WM_DELETE_WINDOW", closeroot)  #使窗口无法关闭

    l1 = tk.Label(root, text='问你一个问题呀', font=('微软雅黑', 14), fg='red' )#第一行第一句话，可以根据自己的需要调整字体大小和想写的话
    l1.grid()
    l2 = tk.Label(root, text='你喜欢我吗？', font=('微软雅黑', 25), fg='blue') #第二行第一句话，可以根据自己的需要调整字体大小和想写的话
    l2.grid(row=1, column=1, sticky=tk.E)
    bm = ImageTk.PhotoImage(file='./test.jpg')  ##加载图片，记得把图片放到程序运行的文件夹
    l3 = tk.Label(root, image=bm)
    l3.grid(row=2, columnspan=2)
    b1 = tk.Button(root, text='喜欢', width=18, height=2, command=Love) #加入“喜欢”的按钮和点击的动作
    b1.grid(row=3, column=0, sticky=tk.W)
    b2 = tk.Button(root, text='不喜欢', width=4, height=1, command=nolove)  #加入“不喜欢”的按钮和点击的动作
    b2.grid(row=3, column=3, sticky=tk.E)

    root.mainloop()    #保持窗口

