# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 10:17
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : examinbill.py


import json
import requests
import os

class examinbill:
    def __init__(self):
        self.baseurl='https://scmsuper.xiyunerp.com/'
        self.loginservice='scmx/user/login.do'
        self.loginurl=os.path.join(self.baseurl,self.loginservice)
        data={
            "account":"qladmin",
            "password":"qianlian123",
            "platform":1,
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


    #获取待审核订单
    def getbilltoexaim(self):
        self.getbilltoexaimserver=''
        self.getbilltoexaimurl=os.path.join(self.baseurl,self.getbilltoexaimserver)
        self.getbilltoexaimserverparams={
            "pageSize":50,
            "currentPage": 1,
            "timeArr":"",
            "warehouseName":"",
            "billDateEnd":"",
            "billDateStart":"",
            "billStatus" :0,
            "billNo":""
        }

        self.todata=json.dumps(self.getbilltoexaimserverparams)

        try:
            res=requests.get(self.getbilltoexaimurl,params=self.todata,headers=self.header).json()
            print(res)
        except Exception as e:
            print(e)

        pass

