# coding:gbk
# 新建一个窗体程序
# 导入tkinter
import tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import *
import os

import main

translate_english_hanzi = {}
translate_hanzi_english = {}
words = []
Chinese = []
file = open('word.txt', 'r', encoding='gbk')
for line in file.readlines():
    i = 0
    line = line.strip()
    k = line.split(' ')[0]
    v = line.split(' ')[1]
    words.append(v)
    Chinese.append(k)
    translate_hanzi_english[k] = v
    translate_english_hanzi[v] = k
file.close()

def change1():
    nW.destroy()
    os.system("python Memory.py")

def change2():
    nW.destroy()
    os.system("python Word_view.py")
def change3():
    nW.destroy()
    os.system("python Word_View")

nW = tk.Tk()

nW.title('Memory')  # 窗口标题
nW.geometry("400x200")  # 窗口尺寸
nW.resizable(width=False, height=False)
# 添加button按钮
# 添加消息框
main_menu = Menu(nW)
main_menu.add_command(label="背单词", command=change1)
main_menu.add_command(label="添加单词")
main_menu.add_command(label="查看单词列表", command=change2)
main_menu.add_command(label="汉译英",command=change3)
nW.config(menu=main_menu)


var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(nW, text="请输入单词:", bg='green', fg='white', font=('Arial', 10), width=20, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.grid(row=0, padx='10', pady='10')
l1 = tk.Label(nW, text="请输入释义:", bg='green', fg='white', font=('Arial', 10), width=20, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l1.grid(row=1)
entry1 = tk.Entry(nW)
entry2 = tk.Entry(nW)
entry1.grid(row=0, column=1, padx='10', pady='10')
entry2.grid(row=1, column=1, padx='10', pady='10')

def click_this():
    new_value = entry1.get()
    new_key = entry2.get()
    translate_english_hanzi[new_key] = new_value
    translate_hanzi_english[new_value] = new_key
    words.append(new_key)
    Chinese.append(new_value)
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    file = open('word.txt', 'w')
    for k, v in translate_hanzi_english.items():
        file.write(str(k) + ' ' + str(v) + '\n')
    file.close()
    tk.messagebox.showinfo(title='display_messagebox',message='添加成功')  # 消息提醒弹窗，点击确定返回值为 ok


b = tk.Button(nW, text='点击保存', font=('Arial', 12), width=10, height=1, command=click_this)

b.grid(row=2, column=1, padx='10', pady='10')
nW.mainloop()
