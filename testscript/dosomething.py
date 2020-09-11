# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 17:51
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : dosomething.py



import os
import requests
import json


class Dosomething:

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


    def updataperchers(self):
        self.updataserver='oms/purchasePrice/updatePurchasePriceOfLocal.do'
        self.updataurl=os.path.join(self.baseurl,self.updataserver)
        with open(r'D:\python\pythonfile\testscript\问题价目_更新结构.txt') as f:
            tent=f.readlines()
            i=1
            for item in tent:
                data=json.dumps(eval(item))
                # print(data,type(data))
                try:
                    res=requests.post(url=self.updataurl,data=data,headers=self.header,verify=False).json()
                    print('执行成功+%s'%i,res)
                except Exception as e:
                    print('执行失败',e)
                i+=1






if __name__ =='__main__':
    d=Dosomething()
    d.updataperchers()

