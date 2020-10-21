# -*- coding: utf-8 -*-
"""
@Time       : 2020/10/21 23:07
@Author     : weilinlin
@File       : smtpSendHtmlEmail.py
@Product    : PyCharm
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import TEST_EMAIL_ADDR


sender = TEST_EMAIL_ADDR
receivers = [TEST_EMAIL_ADDR]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送查看是否ok...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("发件人信息", 'utf-8')
message['To'] = Header("收件人信息", 'utf-8')

subject = 'Python SMTP 邮件'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP(host='smtp.163.com', port=25)
    smtpObj.login(user=TEST_EMAIL_ADDR, password='邮件系统smtp中的授权码')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")
