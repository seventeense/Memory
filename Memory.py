# coding:gbk
import tkinter
from tkinter import messagebox
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import *
import random
import datetime
import os

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
    l = words.index(t)
    if v1.get() == str(Chinese[l]):
        m += 1
        messagebox.showinfo("Memory", "�ش���ȷ! ��ǰ����ȷ��Ϊ��{}".format(m / (n + m)))
    else:
        n += 1
        messagebox.showinfo("Memory", "�ش����! ��ǰ����ȷ��Ϊ��{}".format(m / (n + m)))
    entry1.delete(0, 'end')

def to_memory():
        review_day = []
        times = [2, 5, 8, 15, 30, 60]  # ��ϰ�����������Ϊ��λ
        for a in times:
            review_time = datetime.date.today() + datetime.timedelta(a)  # Ӧ��ϰ��ʱ���
            review_day.append(review_time.strftime("%Y/%m/%d"))
        messagebox.showinfo('Memory','��ϰ��������{}'.format(review_day))


def next_word():
    t = random.choice(words)
    textvar.set(t)

def change1():
    root.destroy()
    os.system("python ADD_WORD.py")

def change2():
    root.destroy()
    os.system("Word_View.py")
def change3():
    root.destroy()
    os.system("python form3.py")
# ������
root = Tk()

root.title("Welcome Memory")
root.geometry("300x400")
root.resizable(width=False, height=False)
root.tk.eval('package require Tix')
root["background"] = "#ADD8E6"

main_menu = Menu(root)
main_menu.add_command(label="������")
main_menu.add_command(label="��ӵ���", command=change1)
main_menu.add_command(label="�鿴�����б�")
main_menu.add_command(label="����Ӣ",command=change3)
root.config(menu=main_menu)


textvar = tkinter.StringVar()
lab1 = Label(root, textvariable=textvar, width=8, height=2, font=("Arial", 25), bg="lightblue")
lab1.place(x=70, y=100)
next_word()

# StringVar�����󶨵�ָ������� ����˫�����
v1 = StringVar()
entry1 = Entry(root, textvariable=v1, width=10)
entry1.place(x=110, y=180)

btn2 = Button(root, text="ȷ��", bg="#ffffff", height=1, width=10, command=vertify)
btn2.place(x=30, y=300)

btn3 = Button(root, text="��һ��", bg="#ffffff", height=1, width=10, command=next_word)
btn3.place(x=190, y=300)

btn4 = Button(root, text="��ϰ�ƻ�", bg="#ffffff", height=1, width=10, command=to_memory)
btn4.place(x=110, y=300)

root.mainloop()
