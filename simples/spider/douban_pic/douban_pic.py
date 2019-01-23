#encoding=utf-8
# python 2.7
#
# 获取豆瓣美女图片
#
import urllib2
import urllib
from bs4 import BeautifulSoup
import os
import time
import requests

def crawl():
    global count
    global counl
    count = 0
    # url = 'https://www.dbmeinv.com/index.htm'所有
    # 选择channel
    for i in range(4,7):
        #选择对应的页码数
        for j in range(1, 5):
            # 规定url地址
            # 之前的url地址为: url = 'https://www.dbmeinv.com/index.htm?pager_offset=%d' %j
            # url = "https://www.dbmeinv.com/dbgroup/show.htm?cid=%d&pager_offset=%d" %(i,j)
            url = 'https://www.dbmeinv.com/index.htm?cid=%d&pager_offset=%d' %(i, j)

            #伪装头部
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

            #发送Request请求
            req = urllib2.Request(url, headers=headers)

            #获取page页面
            page = urllib2.urlopen(req)

            #输出获取得到的页面
            contents = page.read()

            #使用soup解析html页面
            soup = BeautifulSoup(contents, 'lxml')

            # 指定规则在contents中找到我们想要的网络资源
            chou_girl = soup.find_all("img")

            # filename = 'write_data-web.txt'
            # with open(filename, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            #     f.write(link)
            #     f.write(title.encode("utf-8"))
            #     f.write("\n*************************************************************************************************\n")
            # 初始化count
            # 将图片写入到我们的程序所在的当前文件夹中去
            count = 0
            # print type(chou_girl)

            # 遍历每一个元素

            for girl in chou_girl:
                counl = 0
                # 获取其中每个img标签中的src属性，即它的文件地址
                link = girl.get("src")
                
                """
	                字符串在python程序中时unicode编码格式，
	                如果需要处理首先需要转换为utf-8格式
	                如果需要和磁盘打交道，写入到硬盘中使用utf-8格式
	                如果写入到文件中，使用with open打开，使用unicode编码格式
                """
                # 获取标题，以后可以作为图片文件的名字来使用
                title = girl.get("title")
                title = title.encode('utf-8')
                title = title.replace('.', '')
                title = title.replace("?", "？")
                title = title.replace('"', '“')
                title = title.replace('/', '')
                title = title.replace('%', '')
                title = title.decode('utf-8')

                # 计数，方便我们统计共有多少个文件被下载。。注意一点就是如果文件重名了，，后面的文件将会覆盖之前下载的文件。
                count += 1

                # print type(title)
                print '第{}channel中第{}页的第{}张图片\t'.format(i, j, count) + title.encode("utf-8"),
                print link
                response = urllib2.urlopen(link)
                img = response.read()

                # 判断是否已经存在同名文件，如果存在，就通过在名称后添加数字的方式进行命名
                if not os.path.exists('img/{}.jpg'.format(title.encode("utf-8"))):
                    counl = 0
                    with open('img/%d-%d-%d-%s_%d.jpg' % (i, j, count, title, counl), 'wb') as f:
                        f.write(img)
                        f.close()
                elif os.path.exists('img/{}.jpg'.format(title.encode("utf-8"))):
                    counl += 1
                    with open('img/%d-%d-%d-%s_%d.jpg' % (i, j, count, title, counl), 'wb') as f:
                        f.write(img)
                        f.close()
            # 获取完一页中所有的图片信息后，休息2秒钟
            time.sleep(2)
        # 获取完一个类别中设置的所有页面的图片后，休息3秒钟
        time.sleep(3)

#确保本文件如果被当作库文件引用时,只会输出结果，里面的内容不会重复输出。
if __name__ == "__main__":
    crawl()