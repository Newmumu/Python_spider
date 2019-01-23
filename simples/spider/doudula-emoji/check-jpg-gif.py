# encoding=utf-8

import random
import requests
import re
from bs4 import BeautifulSoup
import bs4
import os

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
]

kv = {"User-Agent": random.choice(my_headers)}


def getHTMLText(url, headers):
    try:
        random_header = random.choice(headers)
        r = requests.get(url, headers={"User-Agent": random_header}, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print r.text
        return r.text
    except:
        print "爬取失败"


def getImgList(Ilist, html):
    soup = BeautifulSoup(html, "html.parser")

    pattern_img = re.compile(r'data-original="(.+?)"')
    pattern_title = re.compile(r'alt="(.+?)"')
    imgList = re.findall(pattern_img, html)

    titleList = re.findall(pattern_title, html)
    print(len(titleList))
    print(len(imgList))
    print(titleList)
    print(imgList)
    for i in range(len(titleList)):

        titleList[i] = titleList[i].encode('utf-8')

        Ilist.append([imgList[i], titleList[i]])
    return Ilist


def mkdir(i):
    if not os.path.exists('img-0%d' % i):
        os.mkdir('img-0%d' % i)


def printImg(Ilist, page):
    # print len(Ilist)
    for i in range(len(Ilist)):
        img_content = requests.get(Ilist[i][0][:-4]).content
        if ('.jpg' in Ilist[i][0][-10:]):
            with open('img-0%d/%s.jpg' % (page, Ilist[i][1].decode('utf-8')), 'wb') as f:
                f.write(img_content)
                f.close()
        elif ('.gif' in Ilist[i][0][-10:]):
            with open('img-0%d/%s.gif' % (page, Ilist[i][1].decode('utf-8')), 'wb') as f:
                f.write(img_content)
                f.close()


def main(page):
    Ilist = []
    url = "https://www.doutula.com/photo/list/?page=%d" % page
    html = getHTMLText(url, my_headers)
    Ilist = getImgList(Ilist, html)
    mkdir(page)
    printImg(Ilist, page)



if __name__ == "__main__":
    print "开始获取表情包图片..."
    for page in range(3):
        print "开始获取第%d页中的内容..." % page
        main(page)
        print "第%d页的内容获取完毕..." % page
    print "恭喜你，你想要的内容获取完毕！！"