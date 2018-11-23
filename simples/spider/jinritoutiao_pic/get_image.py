# encoding=utf-8
# Created by double lin at 2018/8/20
import json
import requests
import os
import re


# 通过摄影集获取每个摄影集中的所有图片信息并获取链接，通过调用函数进行抓取
def get_imgs(url):
    proxies = {
        'http': 'http://203.93.209.163:53281'
    }
    data = {
        'category': 'gallery_photograthy',
        'utm_source': 'toutiao',
        'max_behot_time': 0,
        'as': 'A1450BE7DA2B798',
        'cp': '5B7A2B975978CE1',
        '_signature': 'T22iuwAAFBjlQuI7EcoHJU9toq'
    }
    headers = {
        'cookie': 'tt_webid=6591779723280385543; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1655751fca85f4-0e74e5b449bc71-3a61430c-1fa400-1655751fcaa30a; CNZZDATA1259612802=1757802041-1534766943-https%253A%252F%252Fwww.baidu.com%252F%7C1534766943; tt_webid=6591779723280385543; csrftoken=870f5504b759455316e7707a4f04ba94; uuid="w:3e58622f96dd4a13bd67eccaa7c5a567"; __tasessionId=q0kfhbs3l1534774335934',
        'referer': 'https://www.toutiao.com/ch/news_image/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    print('开始下载获取并下载图片信息...')
    wb_data = requests.get(url, headers=headers, params=data, proxies=proxies)
    wb_data.encoding = wb_data.apparent_encoding

    # 将json格式数据转换为字典格式
    data = json.loads(wb_data.text)
    gallarys = data['data']

    # 图册的标签
    labels = []

    # 对于每一个图册，查找其中的所有图片信息（找到图片url，然后通过get_info函数获取图片并保存）
    for gallary in gallarys:
        item_id = gallary['item_id']
        item_num = gallary['gallary_image_count']

        for label in gallary['label']:
            labels.append(label)
        gallary_title = gallary['title'].replace('|', '-').replace('~', '').replace('?', '').replace('《', '').replace('》', '')

        # 以图册的名称创建文件夹
        if not os.path.exists(gallary_title):
            os.mkdir(gallary_title)

        # 获取每一个图片的url地址，并获取其中的信息，描述信息，写入到文件info.txt中
        for p in range(item_num):
            image_url = 'https://www.toutiao.com/a' + str(item_id) + '/#p=' + str(p)
            # image_data = requests.get(image_url)
            get_info(gallary_title, image_url, p)

        print('图册' + gallary_title + '内容下载完毕！')


# 获取一个图片的内容，并保存到指定文件夹下
def get_info(folder, url, p):
    # url = 'https://www.toutiao.com/a6625169399537992206/#p=2'

    proxies = {
        'http': 'http://203.93.209.163:53281'
    }

    # 必须添加请求头，否则发送请求成功，但是返回的数据是不正确的
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    wb_data = requests.get(url, headers=headers, proxies=proxies)
    wb_data.encoding = wb_data.apparent_encoding
    # print(wb_data.text)
    data = re.findall(r'JSON.parse(.*?)siblingList:', wb_data.text, re.S)[0].replace('\\', '').replace('("', '').replace(
        '"),', '')
    # print(data)
    img_data = json.loads(data)
    for img_url in img_data['sub_images']:
        url = img_url['url']
        img_content = requests.get(url, headers=headers, proxies=proxies).content
        with open(folder + '/' + str(p) + '.jpg', 'wb') as f:
            f.write(img_content)
            f.close()


if __name__ == '__main__':
    url = 'https://www.toutiao.com/api/pc/feed/'
    get_imgs(url)