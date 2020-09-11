# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 12:52
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : run.py


import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from interfaceTest.core import SendReport

import time

testcase_dir=r'D:\python\pythonfile\interfaceTest\testcase'
report_dir=r'D:\python\pythonfile\interfaceTest\result'
discover=unittest.defaultTestLoader.discover(testcase_dir,pattern='test*.py')

now = time.strftime("%Y-%m_%d_%H_%M_%S")
filename = report_dir + '\\' + now + '_result.html'


if __name__ == "__main__":
    # filename=os.path.join(report_dir,'result.html')
    with open(filename,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='testReport',description='ceshibaogao')
        runner.run(discover)
    # s=SendReport.SendReport()
    # s.sendmsgwithatt()