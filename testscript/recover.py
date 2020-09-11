# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 14:44
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : recover.py

from pyse import Pyse
import unittest
import time

class uiRecover(unittest.TestCase):

    def setUp(self):
        self.driver=Pyse('chrome')
        self.driver.open('http://t5609.xyscm-biz-manager-web.yunzong:12050/#/login')
        self.driver.max_window()
        self.driver.type('class=>userName','yangxuegx')
        time.sleep(0.5)
        self.driver.type('class=>password','y123456')
        time.sleep(0.5)
        self.driver.click('class=>button')
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

    def test_add_customer(self):
        self.driver.click('xpath=>/html/body/div/div[2]/div[1]/div/div/ul/li[7]/div/span') #点击客户管理，弹出下拉框
        time.sleep(0.5)
        self.driver.ciick('xpath=>/html/body/div/div[2]/div[1]/div/div/ul/li[7]/ul/li[1]/span')#点击客户列表
        time.sleep(0.5)
        self.driver.click('xpath=>//*[@id="content"]/div[2]/div[2]/button/span')#点击新增客户
        time.sleep(0.5)
        self.driver.type('xpath=>//*[@id="content"]/div[2]/form/div[1]/div[1]/div[1]/div/div/div/input','自动测试客户一')#输入客客户名称
        time.sleep(0.5)
        self.driver.type('xpath=>//*[@id="content"]/div[2]/form/div[1]/div[1]/div[2]/div/div/div/input','自动执行业务员一')#输入业务员名称
        time.sleep(0.5)
