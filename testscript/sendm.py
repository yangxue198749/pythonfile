# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 16:23
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : sendm.py



import os
import requests
import json
import time


class Dosomething:

    def __init__(self):
        self.baseurl='https://xybp.xiyunfin.com/'
        self.loginservice='xybp/ba/user/login'
        self.loginurl=os.path.join(self.baseurl,self.loginservice)
        data={
            "account":"yangxue",
            "password":"y123456",
            "force":1
            }
        self.header={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie':'JSESSIONID=aaajVyGTOA6G17bjD1g7w'
        }
        self.logindata=json.dumps(data)

        try:
            res=requests.post(url=self.loginurl,data=self.logindata,headers=self.header,verify=False).json()
            # print(res)
            self.header['Authorization'] = res['resultObject']['token']
        except Exception as e:
            print('登陆失败',e)

    def fileread(self):
        self.sserver='xybp/ma/material/notify/detailK3Up'
        self.sendurl=os.path.join(self.baseurl,self.sserver)
        self.params={
            "materialNo":1001011189,
            "sendSysType":3
        }
        with open(r'C:\Users\Think\Desktop\商品.txt') as f:
            data=f.readlines()
            for item in data:
                self.params["materialNo" ]=item.rstrip('\n')
                print(self.params)
                r=requests.get(url=self.sendurl,params=self.params,headers=self.header).json()
                print(r)
                time.sleep(2)


d=Dosomething()
d.fileread()