# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 15:17
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : wmstest.py

import unittest
from pyse import Pyse
import time


class testwarehouseinner(unittest.TestCase):

    def setUp(self):
        self.driver=Pyse('chrome')
        self.driver.open('http://t4567.xyscm-biz-warehouse-web.yunzong:12370/#/login')
        self.driver.max_window()
        self.driver.type('class=>userName','yxadmin1')
        time.sleep(1)
        self.driver.type('class=>password','y123456')
        time.sleep(1)
        self.driver.click('class=>button')

    def tearDown(self):
        self.driver.close()

    def test1(self):
        self.driver.click('xpath=>/html/body/div/div[2]/div[1]/div/div/ul/li[4]/div/span')
        time.sleep(1)
        self.driver.click('xpath=>/html/body/div/div[2]/div[1]/div/div/ul/li[4]/ul/li[3]/span')
        time.sleep(1)
        self.driver.click('xpath=>//*[@id="content"]/div[2]/div[1]/button/span')#点击新增
        time.sleep(1)
        self.driver.click('xpath=>//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div[1]/div/div/div/span/span/i')#点击下拉框
        time.sleep(1)
        self.driver.click('xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
        time.sleep(1)
        self.driver.type('xpath=>//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div[2]/div/div[1]/input','test1')
        time.sleep(1)
        self.driver.type('xpath=>//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div[3]/div/div[1]/input','test001')
        time.sleep(1)
        self.driver.click('xpath=>//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div[4]/div/div/div/input')
        time.sleep(1)
        self.driver.click('xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
        time.sleep(1)
        self.driver.click('xpath=>//*[@id="content"]/div[2]/div[2]/div/div[2]/form/div[5]/div/button')
        time.sleep(4)

if __name__=="__main__":
    unittest.main()
