## 使用python+Tkinter库构建GUI应用工具 - 个性签名工具

### 安装Tkinter及pillow库

```python
pip install tkinter     # 安装tkinter库
pip install pillow      # 安装pillow库，方便出里图片 使用PIL
```

### 构建GUI程序（具体的网站及程序源码，参考B站UP主**小衬衫**)

具体的信息，在源代码中进行注释
```python
# encoding:utf8
"""
__author__ : weilinlin
__file__   : 个性签名工具
__time__   : 2020-12-16
"""
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import requests

root = Tk()
root.title('Tkinter签名工具')
root.resizable(0, 0)  # 此处设置主窗口是否可以进行大小调整，其中的两个参数分别为width方向和height方向上，值为boolean类型
option = '1.艺术签 2.连笔签 3.商务签 4.楷书签 5.潇洒签 6.草体签 7.行书签 8.个性签 9.可爱签'  # 定义可以使用的字体类型（和传递参数中的ttf保持一致）
var1 = StringVar(value='')  # 定义字符串变量，存储名字
var2 = StringVar(value='')  # 定义字符串变量，存储签字类型选项


def check():
    """
    判断GUI页面中传入的变量是否符合类型，并进行相应的告警内容
    :return:
    """
    name = entry1.get()
    num = entry2.get()
    flag = True
    if num.isdigit():
        num = int(num)
    if name == '':
        var1.set("不能为空")
        flag = False
    if name.isdigit():
        var1.set("不能为数字")
        flag = False
    if type(num) == type(' ') or num == '':
        var2.set("1-9")
        flag = False
    else:
        if num > 9 or num < 1:
            var2.set("1-9")
            flag = False
    if flag:
        get_img(name, num)
    pass


def get_img(name, num, root=root):
    """
    到签字网站获取签名信息，并显示到GUI工具中
    :param name:名字
    :param num:签字类型选项
    :param root:GUI主窗口，句柄
    :return:
    """
    try:
        # 选择接口样式
        signature = ['1.ttf', 'zql.ttf', '8.ttf', '6.tff', 'bzcs.ttf', 'lfc.ttf', '2.ttf', '3.ttf', 'yqk.ttf']
        url = 'http://www.uusty.com/'
        data = {
            'word': name,
            'sizes': 60,
            'fonts': signature[num],
            'fontcolor': '#000000'
        }
        response = requests.post(url, data)
        response.encoding = 'utf-8'
        # print(response.text)
        imgXpath = r'ZWNBSP<img src="(.*?)"/>'
        imgUrls = re.findall(imgXpath, response.text)
        content = requests.get(url + imgUrls[0]).content
        with open('().gif'.format(name), 'wb') as f:
            f.write(content)
        bg_img = ImageTk.PhotoImage(file='().gif'.format(name))
        label = Label(root, Image=bg_img)
        label.bg_img = bg_img
        label.grid(row=2, columnspan=4)
    except:
        messagebox.showinfo("提示", message='生成失败')
    pass


label1 = Label(root, text=option, font=('黑体', 13))
label2 = Label(root, text='输入你的名字：', font=('黑体', 13))
entry1 = Entry(root, width=40, font=('黑体', 13), textvariable=var1)
entry2 = Entry(root, width=10, font=('黑体', 13), textvariable=var2)
button = Button(root, text='确定', command=lambda: check())
label1.grid(row=0, columnspan=3)
label2.grid(row=1, column=0)
entry1.grid(row=1, column=1)
entry2.grid(row=1, column=2)
button.grid(row=1, column=3)
root.mainloop()

```
