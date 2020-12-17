### 附带了帮助信息的工具源代码
```python
# encoding:utf8
"""
__author__ : weilinlin
__file__   : RegexTool
__time__   : 2020-12-16
"""
from tkinter import *
from tkinter import messagebox, ttk
import re

root = Tk()
root.title("RegexTool")
root.resizable(0, 0)


def init():
    """
    构造GUI初始化页面
    TODO: 长度最大匹配长度判断逻辑尚未补充
    TODO: 常用正则表达式列表
    :return:
    """
    button00 = Button(root, width=12, text="( )", command=lambda: (
    text1.insert('insert', "()"), text4.delete("1.0", END), text4.insert("insert", "(re): 对正则表达式分组并记住匹配的文本")))
    button01 = Button(root, width=12, text="[ ]", command=lambda: (
    text1.insert('insert', "[]"), text4.delete("1.0", END), text4.insert("insert", "[...]: 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'")))
    button02 = Button(root, width=12, text="{ }", command=lambda: (text1.insert('insert', "{}"), text4.delete("1.0", END),
                                                                   text4.insert("insert",
                                                                                """re{ n}: 精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。\nre{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。""")))
    # button03 = Button(root, width=12, text="( )", command=lambda: text1.insert('insert', "()"))
    # button04 = Button(root, width=12, text="( )", command=lambda: text1.insert('insert', "()"))
    label03 = Label(root, width=12, text="长度")
    button04 = Button(root, width=12, text="{1, 15}", command=lambda: (
    text1.insert('insert', "{1,15}"), text4.delete("1.0", END), text4.insert("insert", "re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式")))

    button10 = Button(root, width=12, text="*",
                      command=lambda: (text1.insert('insert', "*"), text4.delete("1.0", END), text4.insert("insert", "匹配0个或多个的表达式。")))
    button11 = Button(root, width=12, text="+",
                      command=lambda: (text1.insert('insert', "+"), text4.delete("1.0", END), text4.insert("insert", "匹配1个或多个的表达式。")))
    button12 = Button(root, width=12, text="?", command=lambda: (
    text1.insert('insert', "?"), text4.delete("1.0", END), text4.insert("insert", "匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式。")))
    button13 = Button(root, width=12, text=".", command=lambda: (
    text1.insert('insert', "."), text4.delete("1.0", END), text4.insert("insert", "匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。")))
    button14 = Button(root, width=12, text="-", command=lambda: (text1.insert('insert', "-"), text4.delete("1.0", END),
                                                                 text4.insert("insert",
                                                                              "标识两者之间的内容也可以被匹配，连接作用；如[0-9]，匹配可以匹配0,1,2,3,4,5,6,7,8,9。")))

    button20 = Button(root, width=12, text="0-9", command=lambda: (
    text1.insert('insert', "0-9"), text4.delete("1.0", END), text4.insert("insert", "匹配任何数字。类似于 [0123456789]")))
    button21 = Button(root, width=12, text="a-z", command=lambda: (
    text1.insert('insert', "a-z"), text4.delete("1.0", END), text4.insert("insert", "匹配任何小写字母。类似于 [0123456789]")))
    button22 = Button(root, width=12, text="A-Z", command=lambda: (
    text1.insert('insert', "A-Z"), text4.delete("1.0", END), text4.insert("insert", "匹配任何大写字母。类似于 [0123456789]")))
    button23 = Button(root, width=12, text="^",
                      command=lambda: (text1.insert('insert', "^"), text4.delete("1.0", END), text4.insert("insert", "匹配字符串的开头")))
    button24 = Button(root, width=12, text="$",
                      command=lambda: (text1.insert('insert', "$"), text4.delete("1.0", END), text4.insert("insert", "匹配字符串的末尾")))

    button30 = Button(root, width=12, text="\w", command=lambda: (
    text1.insert('insert', "\w"), text4.delete("1.0", END), text4.insert("insert", "匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。")))
    button31 = Button(root, width=12, text="\W", command=lambda: (
    text1.insert('insert', "\W"), text4.delete("1.0", END), text4.insert("insert", "匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。")))
    button32 = Button(root, width=12, text="\d", command=lambda: (
    text1.insert('insert', "\d"), text4.delete("1.0", END), text4.insert("insert", "匹配一个数字字符。等价于 [0-9]。")))
    button33 = Button(root, width=12, text="\D", command=lambda: (
    text1.insert('insert', "\D"), text4.delete("1.0", END), text4.insert("insert", "匹配一个非数字字符。等价于 [^0-9]。")))
    button34 = Button(root, width=12, text="\\r",
                      command=lambda: (text1.insert('insert', "\\r"), text2.insert("insert", 'text2插入内容函数也可执行')))

    button40 = Button(root, width=12, text="\\b", command=lambda: (text1.insert('insert', "\\b"), text4.delete("1.0", END),
                                                                   text4.insert("insert",
                                                                                """匹配一个单词边界，也就是指单词和空格间的位置。例如，'er\b' 可以匹配"never"中的 'er'，但不能匹配 "verb" 中的 'er'。""")))
    button41 = Button(root, width=12, text="\B", command=lambda: (text1.insert('insert', "\B"), text4.delete("1.0", END),
                                                                  text4.insert("insert",
                                                                               """匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。""")))
    button42 = Button(root, width=12, text="\\s", command=lambda: (
    text1.insert('insert', "\s"), text4.delete("1.0", END), text4.insert("insert", "匹配任意空白字符，等价于 [ \\t\\n\\r\\f]。")))
    button43 = Button(root, width=12, text="\S",
                      command=lambda: (text1.insert('insert', "\S"), text4.delete("1.0", END), text4.insert("insert", "匹配任意非空字符")))
    button44 = Button(root, width=12, text="\\n", command=lambda: (
    text1.insert('insert', "\\n"), text4.delete("1.0", END), text4.insert("insert", "匹配一个换行符。匹配一个制表符。等")))

    button50 = Button(root, width=12, text="\\u4e00-\\u9fa5", command=lambda: (
    text1.insert('insert', "\\u4e00-\\u9fa5"), text4.delete("1.0", END), text4.insert("insert", "匹配中文")))
    button51 = Button(root, width=12, text="|", command=lambda: (
    text1.insert('insert', "|"), text4.delete("1.0", END), text4.insert("insert", "a| b	匹配a或b")))
    button52 = Button(root, width=12, text="\\",
                      command=lambda: (text1.insert('insert', "\\"), text4.delete("1.0", END), text4.insert("insert", "转义符")))
    button53 = Button(root, width=12, text="\\v", command=lambda: (text1.insert('insert', "\\v"), text4.delete("1.0", END),
                                                                   text4.insert("insert",
                                                                                "匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \\f\\n\\r\\t\\s]。")))
    button54 = Button(root, width=12, text="\\t", command=lambda: (text1.insert('insert', "\\t"), text4.delete("1.0", END),
                                                                   text4.insert("insert",
                                                                                "匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \\f\\n\\r\\v\\s]。")))

    button60 = Button(root, width=12, text="\\f", command=lambda: (text1.insert('insert', "\\f"), text4.delete("1.0", END),
                                                                   text4.insert("insert",
                                                                                "匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \\t\\n\\r\\v\\s]。")))
    label61 = Label(root, width=12, text="常用正则表达式")
    # 显示可选值列表，另外处理
    button63 = Button(root, width=12, text="测试", command=checkRegex)
    button64 = Button(root, width=12, text="清空", command=clearAll)

    button00.grid(row=0, column=0, padx=5, pady=5)
    button01.grid(row=0, column=1, padx=5, pady=5)
    button02.grid(row=0, column=2, padx=5, pady=5)
    label03.grid(row=0, column=3, padx=5, pady=5)
    button04.grid(row=0, column=4, padx=5, pady=5)
    button10.grid(row=1, column=0, padx=5, pady=5)
    button11.grid(row=1, column=1, padx=5, pady=5)
    button12.grid(row=1, column=2, padx=5, pady=5)
    button13.grid(row=1, column=3, padx=5, pady=5)
    button14.grid(row=1, column=4, padx=5, pady=5)
    button20.grid(row=2, column=0, padx=5, pady=5)
    button21.grid(row=2, column=1, padx=5, pady=5)
    button22.grid(row=2, column=2, padx=5, pady=5)
    button23.grid(row=2, column=3, padx=5, pady=5)
    button24.grid(row=2, column=4, padx=5, pady=5)
    button30.grid(row=3, column=0, padx=5, pady=5)
    button31.grid(row=3, column=1, padx=5, pady=5)
    button32.grid(row=3, column=2, padx=5, pady=5)
    button33.grid(row=3, column=3, padx=5, pady=5)
    button34.grid(row=3, column=4, padx=5, pady=5)
    button40.grid(row=4, column=0, padx=5, pady=5)
    button41.grid(row=4, column=1, padx=5, pady=5)
    button42.grid(row=4, column=2, padx=5, pady=5)
    button43.grid(row=4, column=3, padx=5, pady=5)
    button44.grid(row=4, column=4, padx=5, pady=5)
    button50.grid(row=5, column=0, padx=5, pady=5)
    button51.grid(row=5, column=1, padx=5, pady=5)
    button52.grid(row=5, column=2, padx=5, pady=5)
    button53.grid(row=5, column=3, padx=5, pady=5)
    button54.grid(row=5, column=4, padx=5, pady=5)
    button60.grid(row=6, column=0, padx=5, pady=5)
    label61.grid(row=6, column=1, padx=5, pady=5)
    # 特殊处理可选值列表
    # label62.grid(row=6, column=2, padx=5, pady=5)
    button63.grid(row=6, column=3, padx=5, pady=5)
    button64.grid(row=6, column=4, padx=5, pady=5)


def clearAll():
    """
    清空三个text框，方便下次输入表达式进行匹配计算
    :return:
    """
    text1.delete('1.0', 'end')
    text2.delete('1.0', 'end')
    text3.delete('1.0', 'end')
    text4.delete("1.0", END)
    pass


def go(*args):  # 处理事件，*args表示可变参数
    value = comboxlist.get()
    if value == "网页链接":
        text1.delete('1.0', END)
        text1.insert('insert', '[a-zA-Z]+://[^\s]*')
    if value == "电子邮件":
        text1.delete('1.0', END)
        text1.insert('insert', '[a-zA-Z]+@[a-zA-Z]+.[a-zA-Z]+')
    if value == "身份证号":
        text1.delete('1.0', END)
        text1.insert('insert', '\d{15}|\d{18}')
    if value == "邮政编码":
        text1.delete('1.0', END)
        text1.insert('insert', '[1-9]\d{5}(?!\d)')
    if value == "数字":
        text1.delete('1.0', END)
        text1.insert('insert', '[0-9]*')
    if value == "字母":
        text1.delete('1.0', END)
        text1.insert('insert', '[A-Za-z]+')
    if value == "大写字母":
        text1.delete('1.0', END)
        text1.insert('insert', '[A-Z]+')
    if value == "小写字母":
        text1.delete('1.0', END)
        text1.insert('insert', '[a-z]+')
    if value == "中文":
        text1.delete('1.0', END)
        text1.insert('insert', '[\\u4e00-\\u9fa5]{0,}')
    if value == "密码":
        text1.delete('1.0', END)
        text1.insert('insert', '[a-zA-Z]\w{5,17}')
    if value == "手机号码":
        text1.delete('1.0', END)
        text1.insert('insert', '(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9]\d{8})')
    # print(comboxlist.get())  # 打印选中的值


def listBox():
    """
    构造下拉选框
    :param root:
    :return:
    """
    comboxlist["values"] = ('常用正则', '网页链接', '电子邮件', '身份证号', '邮政编码', '数字', '字母', '大写字母', '小写字母', '中文', '密码', '手机号码')
    comboxlist.current(0)  # 选择第一个
    comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist.grid(row=6, column=2, padx=5, pady=5)
    pass


def checkRegex():
    """
    根据传入的正则表达式和字符串，输出匹配结果
    :return:
    """
    text3.delete('1.0', 'end')  # 重新开始时，清空原有结果文本框中的所有内容
    var01 = text1.get('1.0', '1.end')  # 获取正则表达式文本框中的内容，一行显示
    var02 = text2.get('1.0', END)  # 获取传递文本框中的所有内容，可以多行
    print("var01", var01)
    try:
        pattern = re.compile('%s' % var01)  # 根据传入的正则表达式字符串，生成正则表达式
        print(pattern)
        result = re.findall(pattern, var02)  # 调用re模块实现正则匹配
        if result:
            print(result)
            # 如果匹配结果不为空，那么循环输出正则匹配结果
            for res in result:
                if res != '':
                    text3.insert(END, res + '\n')
        else:  # 如果匹配失败，在结果框中显示提示信息
            text3.delete('1.0', 'end')
            text3.insert('insert', '正则匹配结果为空')
    except:
        text3.delete('1.0', 'end')
        text3.insert('insert', '匹配失败')


init()  # 初始化窗口

comvalue = StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(root, width=12, textvariable=comvalue)  # 初始化
listBox()  # 构建下拉菜单，显示常用正则表达式

label1 = Label(root, text="正则表达式", font=('黑体', 13))
label2 = Label(root, text="目标字符串", font=('黑体', 13))
label3 = Label(root, text="匹配结果", font=('黑体', 13))
label4 = Label(root, text="帮助信息", font=('黑体', 13))
text1 = Text(root, width=40, height=5, font=('黑体', 13))
text2 = Text(root, width=40, height=5, font=('黑体', 13))
text3 = Text(root, width=40, height=5, font=('黑体', 13))
text4 = Text(root, width=40, height=4, font=('黑体', 13))

label1.grid(row=7, column=0)
text1.grid(row=8, columnspan=6, pady=10)
label2.grid(row=9, column=0)
text2.grid(row=10, columnspan=6, pady=10)
label3.grid(row=11, column=0)
text3.grid(row=12, columnspan=6, pady=10)
label4.grid(row=13, column=0)
text4.grid(row=14, columnspan=6, pady=15)
root.mainloop()

```
