# -*- coding: utf-8 -*-
"""
@Time       : 2020/10/21 21:54
@Author     : weilinlin
@File       : smtpSendTextEmail.py
@Product    : PyCharm
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import TEST_EMAIL_ADDR


sender = TEST_EMAIL_ADDR
receivers = [TEST_EMAIL_ADDR]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('邮件主体内容清单，请收到信息后及时回复', 'plain', 'utf-8')
message['From'] = Header("测试发送邮件", 'utf-8')  # 发送者（显示在邮件头部的发件人信息）
message['To'] = Header("测试接收邮件", 'utf-8')  # 接收者（显示在邮件头部的收件人信息）

subject = 'SMTP 邮件主题002'  # 邮件主题
message['Subject'] = Header(subject, 'utf-8')  # 将邮件主题绑定在邮件message主体上

try:
    smtpObj = smtplib.SMTP(host='smtp.163.com', port=25)
    smtpObj.login(user=TEST_EMAIL_ADDR, password='邮件系统smtp中的授权码')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")
