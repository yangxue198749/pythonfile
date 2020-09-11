#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : SendReport.py
@Author: yangxue
@Date  : 2019/4/28 9:31
@Desc  : 
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from interfaceTest.core import ReadCofig
import os
from interfaceTest.core import Mailsend

mail=ReadCofig.ReadConfig()
mail_data=mail.get_item('sendmail')


class SendReport:
    def __init__(self):
        self.stmpserver=mail_data['mailsever']
        self._user=mail_data['user']
        self._password=mail_data['password']
        self._subject=mail_data['subject']
        self._from=mail_data['from']
        self._to=["yyl_yunlong@126.com","13522069018@126.com","812529856@qq.com"]
        self._report_dir=mail_data['report_dir']
        self._content=mail_data['content']
        self.sendto = ','.join(self._to)

    def New_report(self):
        self._report_lists=os.listdir(self._report_dir)
        self._report_lists.sort(key=lambda fn:os.path.getmtime(self._report_dir+'\\'+fn))
        self.new_report=os.path.join(self._report_dir,self._report_lists[-1])

    def send_mail(self):

        self.New_report()
        self.sendfile = open(self.new_report, 'rb').read()
        # print(self.file)
        self.att = MIMEText(self.sendfile, 'html', 'utf-8')
        self.att['Content-Type'] = 'application/octet-stream'
        self.att['Content-Disposition'] = 'attachment;filename="result.html"'
        self.msgRoot = MIMEMultipart('related')
        self.msgRoot['Subject'] = Header(self._subject, 'utf-8')
        self.msgRoot['From'] = self._from
        self.msgRoot['To'] = self.sendto
        self.msgRoot.attach(self.att)
        print(self.msgRoot.as_string())

        self.smtp=smtplib.SMTP()
        self.smtp.connect(self.stmpserver)
        self.smtp.login(self._user,self._password)
        self.smtp.sendmail(self._from,self._to,self.msgRoot.as_string())
        self.smtp.quit()

    def sendmail(self, msg):
        try:
            self.smtp = smtplib.SMTP()
            self.smtp.connect(self.stmpserver)

        except Exception as e:
            # loger.error('fail')
            print(e)
        try:
            self.smtp.login(self._user, self._password)
        except Exception as e:
            print('login fail', e)
        try:
            self.smtp.sendmail(self._from, self.sendto, msg)
        except Exception as e:
            print('send fail', e)
        self.smtp.quit()

    def sendmsgwithatt(self):
        self.New_report()
        self.file=os.path.basename(self.new_report)
        self.sendto = ','.join(self._to)
        self.sendfile = open(self.new_report, 'rb').read()
        self.att = MIMEText(self.sendfile, 'html', 'utf-8')
        self.att['Content-Type'] = 'application/octet-stream'
        self.att['Content-Disposition'] = 'addachment;filename="%s"'%self.file
        self.msgRoot = MIMEMultipart('related')
        self.msgRoot['Subject'] = Header(self._subject, 'utf-8')
        self.msgRoot['From'] = self._from
        self.msgRoot['To'] = self.sendto
        self.msgRoot.attach(self.att)
        self.smtp = smtplib.SMTP()
        self.smtp.connect(self.stmpserver)
        self.smtp.login(self._user, self._password)
        self.smtp.sendmail(self._from, self._to, self.msgRoot.as_string())
        self.smtp.quit()

#
# s=SendReport()
# s.sendmsgwithatt()
# # s.send_mail()
