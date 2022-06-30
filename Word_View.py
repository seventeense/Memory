# coding:gbk
import tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import *
import os

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
    window.destroy()
    os.system("python Memory.py")

def change2():
    window.destroy()
    os.system("python ADD_WORD.py")
def change3():
    window.destroy()
    os.system("python form3.py")

window = tk.Tk()

window.title('My Window')
window.geometry('500x300')
window.resizable(width=False, height=False)

main_menu = Menu(window)
main_menu.add_command(label="背单词", command=change1)
main_menu.add_command(label="添加单词", command=change2)
main_menu.add_command(label="查看单词列表")
main_menu.add_command(label="汉译英",command=change3)
window.config(menu=main_menu)


def income():
    print("单词列表：{}".format(translate_english_hanzi))
    t.insert("end", str(translate_english_hanzi))


# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tk.Text(window, height=20)
t.pack()
b1 = tk.Button(window, text='显示', width=10,
               height=2, command=income)
b1.pack()
# 第8步，主窗口循环显示
window.mainloop()
