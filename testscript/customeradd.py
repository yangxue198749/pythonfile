# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 18:46
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : customeradd.py

import requests
import os
import json
from urllib3 import encode_multipart_formdata
from testscript.scriptData import Data #根目录下引入数据体 数据代码分离


class customerAdd:
    def __init__(self):
        '''
        基础url 共用的在其他方式也可使用，根据项目跟改，自己url是本链接的url
        data 是请求的数据，force:0 非强制登陆，1：强制登陆
        登陆完成后把返回的token，赋值到header中的Authorization，供其他模块使用
        '''
        self.baseurl='https://scmubpre.xiyunfin.com/'
        self.url=os.path.join(self.baseurl,'ub/user/login')
        print(self.url)
        data = {
            "account": "agent.ql.admin",
            "password": "123456",
            "force": 1
        }
        self.data=json.dumps(data)
        self.header={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json'
        }
        try:
            res=requests.post(url=self.url,headers=self.header,data=self.data).json()
            self.header['Authorization'] = res['resultObject']['token']
        except Exception as e:
            print('登陆失败',e)
        self.d=Data()


    def newwarehose(self,warehosename):
        '''
        新增仓库函数
        :param warehosename:仓名称参数
        :return:没有返回值，直接把请求返回放到了类中
        wdata:从数据源中取数据
        '''
        url=os.path.join(self.baseurl,'ub/agent/base/warehouse/newWarehouse')
        wdata=self.d.wdata()
        wdata['warehouseName']=warehosename
        self.wdata=json.dumps(wdata)
        try:
            self.warehoseres=requests.post(url=url,headers=self.header,data=self.wdata).json()
            print('新增仓库成功： ',self.warehoseres['resultObject']['warehouseName'])
        except Exception as e:
            print('新建仓库失败',e)

    def addcustomer(self):
        '''
        新增客户函数
        data=self.d.cdata()：从数据源中取数据
        dk = self.imagedo()：从图片处理函数中获取图片上传后的key，用于图片的上传校验
        warehosename='仓库00%s-y'%i：设置仓库名称,可修改除了%s之外的命名
        customername='客户00%s-y'%i：设置客户名称,可修改除了%s之外的命名
        :return:
        '''
        self.url=os.path.join(self.baseurl,'ub/agent/base/customer/add')
        data=self.d.cdata()
        for i in range(9):
            dk = self.imagedo('1')
            if dk:
                data['businessCommonFiles'][0]['key'] = dk['2']
                data['legalCommonFiles'][0]['key'] = dk['3']
                data['foodSafetyCommonFiles'][0]['key'] = dk['11']
                warehosename='预发仓库%s'%i
                customername='预发客户%s'%i
                self.newwarehose(warehosename)
                if self.warehoseres:
                    data['warehouseId']=self.warehoseres['resultObject']['warehouseId']
                    data['warehouseNumber']=self.warehoseres['resultObject']['warehouseNumber']
                    data['warehouseName']=self.warehoseres['resultObject']['warehouseName']
                    data['customerName']=customername
                    self.dataf = json.dumps(data)
                    try:
                        self.customerres=requests.post(url=self.url,headers=self.header,data=self.dataf).json()
                        print('新增客户成功',self.customerres)
                    except Exception as e:
                        print('新增客户失败',e)


    def supplieradd(self):
        '''
        供应商跟客户绑成一对一，通过客户名模糊搜索出来，列表里把客户名称提出来，供应商名称“客户名称+供应商”
        拿到客户对应得仓库编号再拿到仓库id，然后绑定到一起
        使用哦得时候修改一下customerlist=self.getcustomer(50,'模糊搜索客户名')，之前建了什么客户模糊搜索一下就好
        然后代码会自动建供应商，大致是这样名称得供应商‘客户名称供应商’
        :return:
        '''
        url=os.path.join(self.baseurl,'ub/agent/base/supplier/submit')
        customerlist=self.getcustomer(50,'预发客户')
        listsupplier=[]
        for itme in customerlist:
            dict={}
            dict['cname']=itme['customerName']
            dict['wid']=itme['warehouseId']
            listsupplier.append(dict)

        sdata=self.d.supplier()

        for itme in listsupplier:
            dk=self.imagedo('2')
            if dk:
                sdata['businessCommonFiles'][0]['key'] = dk['2']
                sdata['legalCommonFiles'][0]['key'] = dk['3']
                sdata['foodSafetyCommonFiles'][0]['key'] = dk['11']
                sdata['transactionInvoice'][0]['key']=dk['12']
                sdata['businessContract'][0]['key'] = dk['13']
                sdata['supplierName']=(itme['cname']+'供应商')
                sdata['warehouseIds'][0]=itme['wid']
                self.sdata=json.dumps(sdata)
                # print(self.sdata)
                try:
                    res=requests.post(url=url,headers=self.header,data=self.sdata).json()
                    print('新增供应商成功,编号：',res)
                except Exception as e:
                    print('新增失败：',e)


    #获取用户得接口
    def getcustomer(self,pagesize,customername):
        self.url=os.path.join(self.baseurl,'ub/agent/base/customer/page')
        params={
                   'pageSize':pagesize,
                   'currentPage':1,
                   'totalCount':0,
                   'customerName':customername,
                   'status':'',
                   'warehouseName':'',
                   'companyType':''
              }
        try:
            res=requests.get(url=self.url,headers=self.header,params=params).json()
            clist=res['resultObject']['pageData']
            # print(clist)
            return clist
        except Exception as e:
            print('获取客户失败：',e)


    def imagedo(self,role):
        '''
        处理图片信息函数
        主要处理图片上传后返回一个key
        role：客户：1 供应商：2
        :return:
        '''
        url=os.path.join(self.baseurl,'ub/image/cache/upload')
        header={
            'Authorization':'09091ca4b0534cbfb57ff6d49c115d83',
            'Accept-Encoding':'gzip, deflate'
        }
        filename='1.png'
        filepath=r'C:\Users\Think\Desktop\img\1.png'
        header['Authorization']=self.header['Authorization']
        if role =='1':
            dictkey={}
            for i in (2,3,11):
                data={}
                data['type']=i
                data['file'] = (filename, open(filepath, 'rb').read())
                encode_data = encode_multipart_formdata(data)
                data = encode_data[0]
                header['Content-Type'] = encode_data[1]
                try:
                    res=requests.post(url=url,headers=header,data=data).json()
                    dictkey['%s'%i]=res['resultObject']['key']
                except Exception as e:
                    print('图片上传失败',e)
            return dictkey

        elif role =='2':
            dictkey={}
            for i in (2,3,11,12,13):
                data={}
                data['type']=i
                data['file'] = (filename, open(filepath, 'rb').read())
                encode_data = encode_multipart_formdata(data)
                data = encode_data[0]
                header['Content-Type'] = encode_data[1]
                try:
                    res=requests.post(url=url,headers=header,data=data).json()
                    dictkey['%s'%i]=res['resultObject']['key']
                except Exception as e:
                    print('图片上传失败',e)
            return dictkey
        else:
            print('未知的业务模式')





if __name__=='__main__':
    c=customerAdd()
    c.supplieradd()
    # c.addcustomer()
