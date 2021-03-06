import tkinter
from tkinter import messagebox
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import *
import random

# 导入文件
words = []
Chinese = []
file = open('word.txt', 'r', encoding='gbk')
for line in file.readlines():
    line = line.strip()
    k = line.split(' ')[0]
    v = line.split(' ')[1]
    words.append(v)
    Chinese.append(k)
file.close()

m = 0
n = 0


def vertify():
    global m
    global n
    t = textvar.get()
    l = words.index(t)
    if v1.get() == str(Chinese[l]):
        m += 1
        messagebox.showinfo("Memory", "回答正确! 当前的正确率为：{}".format(m / (n + m)))
    else:
        n += 1
        messagebox.showinfo("Memory", "回答错误! 当前的正确率为：{}".format(m / (n + m)))


def next_word():
    t = random.choice(words)
    textvar.set(t)


# 主界面
root = Tk()

root.title("Welcome Memory")
root.geometry("300x400")
root.resizable(width=False, height=False)
root.tk.eval('package require Tix')
root["background"] = "#ADD8E6"

textvar = tkinter.StringVar()
lab1 = Label(root, textvariable=textvar, width=8, height=2, font=("Arial", 25), bg="lightblue")
lab1.place(x=70, y=100)
next_word()

# StringVar变量绑定到指定的组件 两者双向关联
v1 = StringVar()
entry1 = Entry(root, textvariable=v1, width=10)
entry1.place(x=110, y=180)

btn2 = Button(root, text="确定", bg="#ffffff", height=1, width=10, command=vertify)
btn2.place(x=30, y=300)

btn3 = Button(root, text="下一个", bg="#ffffff", height=1, width=10, command=next_word)
btn3.place(x=190, y=300)

root.mainloop()
