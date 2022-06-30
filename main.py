"""
背单词程序：
    1.玩家录入单词
    2.程序提供单词中文，玩家录入英文
    3.根据玩家录入情况判断玩家对每个单词的熟练程度
    4.根据熟练程度设计背单词计划
"""
import datetime
import random as r
import pickle


def _form():
    print("""
                            欢迎来到背单词
            根据English回答汉语 或者根据汉语回答English
            ——————————————————————————————————————
            1.添加单词
            2.English-->>汉语
            3.汉语-->>English
            4.单词列表
            5.计算复习日期
            6.退出程序
    
    
    """)


def review_time(today):
    delta_list = [1, 1, 2, 2, 3, 4, 5, 5]  # 每两天复习的间隔
    review_day = []
    new_day = datetime.datetime.strptime(today, '%m-%d')
    for day in delta_list:
        new_day = datetime.datetime.strptime(new_day.strftime('%m-%d'), '%m-%d') + datetime.timedelta(days=day)
        review_day.append(new_day.strftime('%m.%d'))
    print('today is ', today, 'review days are', review_day)

    # 1.玩家录入单词:


translate_english_hanzi = {}
translate_hanzi_english = {}
words = []
Chinese = []
file = open('word.txt', 'r', encoding='UTF-8')
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
# words = ["abandon", "private", "insist", "responsibility"]
# Chinese = ["放弃", "海贼", "坚持", "责任心"]
# translate_hanzi_english = {
#     "放弃": "abandon",
#     "海贼": "private",
#     "坚持": "insist",
#     "责任心": "responsibility"
# }
# translate_english_hanzi = {
#     "abandon": "放弃",
#     "private": "海贼",
#     "insist": "坚持",
#     "responsibility": "责任心"
# }

if __name__ == '__main__':
    iscontinue = "y"
    while iscontinue == "y" or iscontinue == "Y":
        _form()
        F = input('请输入功能前的数字:')
        if F == '1':
            continue1 = 'y'
            while continue1 == 'y' or continue1 == 'Y':
                new_value = input('请输入一个新的单词的释义:')
                new_key = input('请输入这个新单词:')
                translate_english_hanzi[new_key] = new_value
                translate_hanzi_english[new_value] = new_key
                words.append(new_key)
                Chinese.append(new_value)
                continue1 = input("是否继续添加单词(Y/N):")
            file=open('word.txt','w')
            for k, v in translate_hanzi_english.items():
                file.write(str(k) + ' ' + str(v) + '\n')
            file.close()
            iscontinue = input("\n\n是否继续（Y/N)：")

        if F == '2':
            continue2 = 'y'
            n = 0
            m = 0
            su = 0
            while continue2 == 'y' or continue2 == 'Y':
                t = r.choice(words)
                print("请输入该单词对应的汉字：{}".format(t))
                l = words.index(t)
                guess = input()
                if guess == Chinese[l]:
                    m += 1
                    print("恭喜你回答正确!", "       正确率为{}".format(m / (n + m)))
                else:
                    n += 1
                    print("对不起，不正确", "       正确率为{}".format(m / (n + m)))
                continue2 = input("是否继续翻译(Y/N):")
            iscontinue = input("\n\n是否继续（Y/N)：")
        if F == '3':
            continue3 = 'y'
            n = 0
            m = 0
            su = 0
            while continue3 == 'y' or continue3 == 'Y':
                t = r.choice(Chinese)
                print("请输入该汉字对应的单词：{}".format(t))
                l = Chinese.index(t)
                guess = input()
                if guess == words[l]:
                    m += 1
                    print("恭喜你回答正确!", "       正确率为{}".format(m / (n + m)))
                else:
                    n += 1
                    print("对不起，不正确", "       正确率为{}".format(m / (n + m)))
                continue3 = input("是否继续翻译(Y/N):")
            iscontinue = input("\n\n是否继续（Y/N)：")
        if F == '4':
            print("单词列表：{}".format(translate_english_hanzi))
            iscontinue = input("\n\n是否继续（Y/N)：")
        if F == '5':
            data1 = input("请输入学习的日期 （格式：08-28）: ")
            review_time(data1)
            iscontinue = input("\n\n是否继续（Y/N)：")

        if F == '6':
            iscontinue = 'N'
