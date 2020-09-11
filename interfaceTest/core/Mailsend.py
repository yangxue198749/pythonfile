#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : mail.py
@Author: yangxue
@Date  : 2019/4/22 16:31
@Desc  :
'''
import unittest
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from interfaceTest.core import ReadCofig
import os

mail=ReadCofig.ReadConfig()
mail_data=mail.get_item('sendmail')



class Mail:
    '''初始化的时候先定义了邮件服务器，用户名和密码'''

    def __init__(self):
        self.mailserver = mail_data['mailsever']
        self._user = mail_data['user']
        self._password = mail_data['password']
        self.subject = mail_data['subject']
        self.sender = mail_data['from']
        self.receiver = mail_data['to']
        self.filepath=mail_data['report_dir']

    def sendmail(self, msg):
        try:
            self.smtp = smtplib.SMTP()
            self.smtp.connect(self.mailserver)

        except Exception as e:

            print(e)
        try:
            self.smtp.login(self._user, self._password)
        except Exception as e:
            print('login fail', e)
        try:
            self.smtp.sendmail(self.sender, self.receiver, msg)
        except Exception as e:
            print('send fail', e)
        self.smtp.quit()

    def sendcontent(self, content):
        self.msg = MIMEText('%s' % content, 'plain', 'utf-8')
        self.sendto = ','.join(self.receiver)
        self.msg['Subject'] = Header(self.subject, 'utf-8')
        self.msg['From'] = self.sender
        self.msg['To'] = self.sendto  # 'yyl_yunlong@126.com'
        self.sendmail(self.msg.as_string())

    def sendmailwithfile(self, filepath):
        self.sendto = ','.join(self.receiver)
        self.file = os.path.basename(filepath)
        self.sendfile = open(filepath, 'rb').read()
        self.att = MIMEText(self.sendfile, 'html', 'utf-8')
        self.att['Content-Type'] = 'application/octet-stream'
        self.att['Content-Disposition'] = 'addachment;filename=%s' % self.file
        self.msgRoot = MIMEMultipart('related')
        self.msgRoot['Subject'] = self.subject
        self.msgRoot['From'] = self.sender
        self.msgRoot['To'] = self.sendto
        print(self.msgRoot.as_string())
        self.msgRoot.attach(self.att)
        self.sendmail(self.msgRoot.as_string())


class send_new_report:
    def new_report(self, report_dir):
        self.base_dir = report_dir
        self.lists = os.listdir(self.base_dir)
        self.lists.sort(key=lambda fn: os.path.getmtime(self.base_dir + '\\' + fn))
        self.report_new = os.path.join(self.base_dir, self.lists[-1])
        return self.report_new

    def product_report(self):
        self.testcase_dir = r'D:\python\testcase\Test'
        self.report_dir = r'D:\python\testcase\Report'
        self.discover = unittest.defaultTestLoader.discover(self.testcase_dir, pattern='test_*.py')
        now = time.strftime("%Y-%m_%d_%H_%M_%S")
        self.filename = self.report_dir + '\\' + now + 'result.html'
        self.fp = open(self.filename, 'wb')
        self.runner = HTMLTestRunner.HTMLTestRunner(stream=self.fp, title='测试报告444', description='用例执行情况')
        self.runner.run(self.discover)
        self.fp.close()
        self.new_rep = self.new_report(self.report_dir)
        rec = ["yyl_yunlong@126.com", '13522069018@126.com', '812529856@qq.com']
        self.sendmail = Mail('smtp.126.com', '13522069018@126.com', 'yx198749', '13522069018@126.com', rec, '测试报告')
        self.sendmail.sendmailwithfile(self.new_rep)


if __name__ == '__main__':
    rec = ["yyl_yunlong@126.com", '13522069018@126.com', '812529856@qq.com']
    m = Mail('smtp.126.com', '13522069018@126.com', 'yx198749', '13522069018@126.com', rec, 'report')
    m.sendmailwithfile(r'D:\python\interfacetest\result\result.html')
    # s=send_new_report()
    # s.product_report()

