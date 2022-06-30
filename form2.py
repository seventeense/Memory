# coding:gbk
import tkinter as tk

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

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')


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
