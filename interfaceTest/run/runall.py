#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : runall.py
@Author: yangxue
@Date  : 2019/5/16 14:49
@Desc  : 
'''

import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from core import SendReport
import time

testcase_dir=r'C:\Users\Think\PycharmProjects\InterfaceTest\testcase'
report_dir=r'C:\Users\Think\PycharmProjects\InterfaceTest\result'
discover=unittest.defaultTestLoader.discover(testcase_dir,pattern='test*.py')

now = time.strftime("%Y-%m_%d_%H_%M_%S")
filename = report_dir + '\\' + now + '_result.html'


if __name__ == "__main__":
    # filename=os.path.join(report_dir,'result.html')
    with open(filename,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='testReport',description='ceshibaogao')
        runner.run(discover)
    s=SendReport.SendReport()
    s.sendmsgwithatt()
