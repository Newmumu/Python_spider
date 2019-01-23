#encoding=utf-8
# import requests
import random
import urllib2
import re
import os

# url = 'https://blog.csdn.net/qq_32670879/article/details/80590615'
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]

def getImageList(url, headers):
    randdom_header = random.choice(headers)
    req = urllib2.Request(url)
    req.add_header("User-Agent", randdom_header)

    # 可以通过类似的方式进行请求域名内容的设置
    # req.add_header("Host", "blog.csdn.net")
    # req.add_header("Referer", "http://blog.csdn.net/")
    # req.add_header("GET", url)

    content = urllib2.urlopen(req).read()

    img_pattern = re.compile(r'data-original="(.+?)"')   #获取图片url地址匹配正则表达式
    alt_pattern = re.compile(r'alt="(.+?)"')        #获取图片标题的对应正则表达式
    imgLink = re.findall(img_pattern, content)      #从content中找到所有的img的url链接地址
    title = re.findall(alt_pattern, content)        #从content中找到所有的img的title名称
    count = 1
    if not os.path.exists(root):
        os.mkdir(root)
    # 获取title的长度即，图片url的长度，然后对其中的每一个内容进行请求，并获取内容进行保存
    for i in range(len(title)):
        count += 1
        img_content = urllib2.urlopen(imgLink[i])

        # 保存数据
        with open(root+'/%s.jpg' % title[i].decode('utf-8'), 'wb') as f:
            #在str类型的数据中才可以使用decode和encode方法，仔细分析这些数据特点，可以借助print type()来获取数据的类型，并进行操作
            f.write(img_content.read())
            f.close()
    # 对每一个页面中的图片进行获取并计数
    print count
if __name__ == "__main__":
    # 循环页面，获取第9和第10页的图片内容
    for page in range(9,11):
        root = "D:\python-workspace\python-pachong\doudula-emoji//img-0%d" % page
        url = 'https://www.doutula.com/photo/list/?page=%d' % page
        getImageList(url, my_headers)