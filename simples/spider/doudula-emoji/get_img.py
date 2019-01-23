#encoding: utf-8
import requests
import os
url = 'https://wx2.sinaimg.cn/bmiddle/0060lm7Tgy1fsraalxba3j30dw0oojv7.jpg'
root = "D:/python-workspace/python-pachong/doudula-emoji/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print "文件保存成功"
    else:
        print "文件已存在"
        with open(path.split('.')[-2]+str('_1')+'.jpg', 'wb') as f:
            r = requests.get(url)
            f.write(r.content)
            f.close()
            print '文件重新保存成功'
    path = path.split('.')[-2] + str('_1') + '.jpg'
    print path
except:
    print "爬取失败"