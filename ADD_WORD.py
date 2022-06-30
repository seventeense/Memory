# coding:gbk
# �½�һ���������
# ����tkinter
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

nW.title('Memory')  # ���ڱ���
nW.geometry("400x200")  # ���ڳߴ�
nW.resizable(width=False, height=False)
# ���button��ť
# �����Ϣ��
main_menu = Menu(nW)
main_menu.add_command(label="������", command=change1)
main_menu.add_command(label="��ӵ���")
main_menu.add_command(label="�鿴�����б�", command=change2)
main_menu.add_command(label="����Ӣ",command=change3)
nW.config(menu=main_menu)


var = tk.StringVar()  # ��label��ǩ����������Ϊ�ַ����ͣ���var������hit_me�����Ĵ�������������ʾ�ڱ�ǩ��
l = tk.Label(nW, text="�����뵥��:", bg='green', fg='white', font=('Arial', 10), width=20, height=2)
# ˵���� bgΪ������fgΪ������ɫ��fontΪ���壬widthΪ����heightΪ�ߣ�����ĳ��͸����ַ��ĳ��͸ߣ�����height=2,���Ǳ�ǩ��2���ַ���ô��
l.grid(row=0, padx='10', pady='10')
l1 = tk.Label(nW, text="����������:", bg='green', fg='white', font=('Arial', 10), width=20, height=2)
# ˵���� bgΪ������fgΪ������ɫ��fontΪ���壬widthΪ����heightΪ�ߣ�����ĳ��͸����ַ��ĳ��͸ߣ�����height=2,���Ǳ�ǩ��2���ַ���ô��
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
    tk.messagebox.showinfo(title='display_messagebox',message='��ӳɹ�')  # ��Ϣ���ѵ��������ȷ������ֵΪ ok


b = tk.Button(nW, text='�������', font=('Arial', 12), width=10, height=1, command=click_this)

b.grid(row=2, column=1, padx='10', pady='10')
nW.mainloop()
