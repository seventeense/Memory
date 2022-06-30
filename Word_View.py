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
main_menu.add_command(label="������", command=change1)
main_menu.add_command(label="��ӵ���", command=change2)
main_menu.add_command(label="�鿴�����б�")
main_menu.add_command(label="����Ӣ",command=change3)
window.config(menu=main_menu)


def income():
    print("�����б�{}".format(translate_english_hanzi))
    t.insert("end", str(translate_english_hanzi))


# ��7��������������һ�������ı���text������ʾ��ָ��height=3Ϊ�ı����������ַ��߶�
t = tk.Text(window, height=20)
t.pack()
b1 = tk.Button(window, text='��ʾ', width=10,
               height=2, command=income)
b1.pack()
# ��8����������ѭ����ʾ
window.mainloop()
