import pyperclip
import requests

f = open("question.txt",encoding='utf-8')
for i in range(6):
    line = f.readline()

import pynput.keyboard as pk


def query(timu):
    url = 'http://cx.icodef.com/wyn-nb?v=3'
    # ex = input("题目:")
    data = {
        'question':timu
    }
    try:
        res = requests.post(url,data).json()
    except:
        pass
    ans = res.get('data')
    if '李恒雅' in ans:
        ans = "未搜索到答案..."
    try:
        ansarr = ans.split('#')
        # for an in ansarr:
        #     print(an)
        for i, value in enumerate(ansarr):
            if value == '正确':
                value = "对"
            elif value == '错误':
                value = "错"
            pyperclip.copy(value)
            print(chr(i + 65), value)
    except:
        print(ans)
    print("----------------")

def write():
    while True:
        url = 'http://cx.icodef.com/wyn-nb?v=3'
        ex = input("请输入题目:")
        print("#")
        data = {
            'question': ex
        }
        try:
            res = requests.post(url, data).json()
        except:
            pass
        ans = res.get('data')
        if '李恒雅' in ans:
            ans = "未搜索到答案..."
        try:
            ansarr = ans.split('#')
            # for an in ansarr:
            #     print(an)
            for i,value in enumerate(ansarr):
                print(chr(i+65),value)
        except:
            print(ans)
        print("----------------")

# 使用readline()读文件
def read():
    # while True:
    line = f.readline()
    if line:
        # que = line.replace("VM1164:5 ","")
        que = line[line.index(' ') + 1:]
        print ("题目:"+que)
        query(que)


def on_press(key):
    # 监听按键
    key=str(key)[1]
    # print("按键为",key)
    if key == 'f':
        read()
# 连接事件以及释放
with pk.Listener(on_press=on_press) as pklistener:
    pklistener.join()