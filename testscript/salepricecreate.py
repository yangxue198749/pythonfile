# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 15:42
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : salepricecreate.py


import requests
import json
import os
from testscript.scriptData import Data



class salepricecreate():
    def __init__(self):
        self.base_url='https://scmubpre.xiyunfin.com/'
        self.login_sevice='ub/user/login'
        self.login_url=os.path.join(self.base_url,self.login_sevice)
        self.data={
            "account": "standard.ql.admin",
            "password": "123456",
            "force": 1
        }

        self.login_data = json.dumps(self.data)
        self.header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json'
        }

        try:
            res=requests.post(url=self.login_url,headers=self.header,data=self.login_data).json()
            self.header['Authorization'] = res['resultObject']['token']
        except Exception as e:
            print('登陆失败',e)

        self.d=Data()


    def get_all_material(self):
        self.get_all_material_sever=''
        self.get_all_material_url=os.path.join(self.base_url,self.get_all_material_sever)


    def add_purches(self):
        self.add_purches_servier=''
        self.add_purches_servier_url=os.path.join(self.base_url,self.add_purches_servier)


    #获取一下仓库下已经新建得采购价目表
    def get_purches(self):
        self.get_purchesservice='ub/standardjc/base/purchasePrice/queryPurchasePricePaging?'
        self.get_purches_url=os.path.join(self.base_url,self.get_purchesservice)
        self.params=self.d.perchersedata()

        try:
            self.perchesrdatares=requests.get(url=self.get_purches_url,headers=self.header,params=self.params).json()
            print('获取成功')
        except Exception as e:
            print('获取失败，',e)

    def get_mentail(self,materialName):
        self.get_materialserver='ub/standardjc/base/material/list?'
        self.get_materialurl=os.path.join(self.base_url,self.get_materialserver)
        self.materialparams=self.d.get_material()
        self.materialparams['materialName']=materialName
        try:
            res=requests.get(url=self.get_materialurl,headers=self.header,params=self.materialparams).json()
            return res['resultObject']['pageData'][0]['saleTaxRate']
        except Exception as e:
            print(e)

    def add_sale(self):
        self.add_service='ub/standardjc/base/salePrice/newSalePrice'
        self.add_url=os.path.join(self.base_url,self.add_service)
        self.data1=self.d.saledata()
        self.get_purches()
        for item in self.perchesrdatares['resultObject']['pageData']:
            self.data1['salePriceDetailList'][0]['materialName']=item['materialName']
            self.data1['salePriceDetailList'][0]['materialNumber']=item['materialNumber']
            self.data1['salePriceDetailList'][0]['materialId'] = item['materialId']
            self.data1['salePriceDetailList'][0]['materialUnitName'] = item['materialUnitName']
            self.data1['salePriceDetailList'][0]['materialUnitNumber'] = item['materialUnitNumber']
            self.data1['salePriceDetailList'][0]['materialSpecification'] = item['materialSpecification']
            self.data1['salePriceDetailList'][0]['saleTaxRate']=self.get_mentail(item['materialName'])
            self.datap=json.dumps(self.data1)
            print(self.datap)

            try:
                res=requests.post(url=self.add_url,data=self.datap,headers=self.header).json()
                print(res)
            except Exception as e:
                print('新增失败',e)

if __name__=='__main__':
    s=salepricecreate()
    s.add_sale()

