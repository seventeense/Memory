# coding:gbk
import os
import tkinter
from tkinter import messagebox
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import *
import random

# �����ļ�
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
    l = Chinese.index(t)
    if v1.get() == str(words[l]):
        m += 1
        messagebox.showinfo("Memory", "�ش���ȷ! ��ǰ����ȷ��Ϊ��{}".format(m / (n + m)))
    else:
        n += 1
        messagebox.showinfo("Memory", "�ش����! ��ǰ����ȷ��Ϊ��{}".format(m / (n + m)))
    entry1.delete(0, 'end')

def next_word():
    t = random.choice(Chinese)
    textvar.set(t)


# ������
form3 = Tk()

form3.title("Welcome Memory")
form3.geometry("300x400")
form3.resizable(width=False, height=False)
form3.tk.eval('package require Tix')
form3["background"] = "#ADD8E6"


def change1():
    form3.destroy()
    os.system("python Memory.py")


def change2():
    form3.destroy()
    os.system("python ADD_WORD.py")

def change3():
    form3.destroy()
    os.system("python Word_View.py")


main_menu = Menu(form3)
main_menu.add_command(label="������", command=change1)
main_menu.add_command(label="��ӵ���", command=change2)
main_menu.add_command(label="�鿴�����б�",command=change3)
main_menu.add_command(label="����Ӣ")
form3.config(menu=main_menu)
textvar = tkinter.StringVar()
lab1 = Label(form3, textvariable=textvar, width=8, height=2, font=("Arial", 25), bg="lightblue")
lab1.place(x=70, y=100)
next_word()

# StringVar�����󶨵�ָ������� ����˫�����
v1 = StringVar()
entry1 = Entry(form3, textvariable=v1, width=10)
entry1.place(x=110, y=180)

btn2 = Button(form3, text="ȷ��", bg="#ffffff", height=1, width=10, command=vertify)
btn2.place(x=30, y=300)

btn3 = Button(form3, text="��һ��", bg="#ffffff", height=1, width=10, command=next_word)
btn3.place(x=190, y=300)

form3.mainloop()
