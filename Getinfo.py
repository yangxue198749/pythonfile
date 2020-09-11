# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 17:33
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : Getinfo.py

import requests
from bs4 import BeautifulSoup



class Getinfo:
    def __init__(self):
        self.baseurl='https://www.qichacha.com/'
        self.headers={
            'User - Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8'
        }

    def gethttp(self):
        pass
