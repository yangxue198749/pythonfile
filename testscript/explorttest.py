# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 10:01
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : explorttest.py


import requests
import os
import json
from testscript.exportdata import Export
from urllib3 import encode_multipart_formdata
import threadpool
from threadpool import ThreadPool

class exportexcl:

    def __init__(self):
        self.baseurl = 'http://crouter.yunzongnet.com/xyscm-biz-backstage/t1294/'
        self.loginservice = 'ub/user/login'
        self.loginurl = os.path.join(self.baseurl, self.loginservice)
        data = {
            "account": "yangxuegx",
            "password": "y123456",
            "force": 1
        }
        self.header = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'JSESSIONID=aaajVyGTOA6G17bjD1g7w'
        }
        self.logindata = json.dumps(data)

        try:
            res = requests.post(url=self.loginurl, data=self.logindata, headers=self.header).json()
            # print(res)
            self.header['Authorization'] = res['resultObject']['token']
        except Exception as e:
            print('登陆失败', e)

        self.e=Export()

    #通用post请求
    def commenpost(self,server,data):
        self.commenserver=server
        self.commerurl=os.path.join(self.baseurl,self.commenserver)
        self.commendata=json.dumps(data)

        try:
            self.commenres=requests.post(url=self.commerurl,headers=self.header,data=self.commendata).json()
            print('success')
            return self.commenres
        except Exception as e:
            print('fail',e)

    #通用get方法
    def commenget(self,server,params):
        self.commenserver = server
        self.commerurl = os.path.join(self.baseurl, self.commenserver)
        self.commerparams = json.dumps(params)
        print(self.commerparams)

        try:
            self.commenres = requests.get(url=self.commerurl, headers=self.header, params=params).json()

            if self.commenres['success']==True:
                print('success')
                return self.commenres
            else:
                print('fail')
        except Exception as e:
            print('执行失败', e)



    #代客下单
    def dkcreatebill(self):
        self.dkserver='ub/standardjc/bill/csrPurchaseBill/addJcCsrPurchaseBill'
        self.data=self.e.exportsaleBilldata()
        for i in range(10):
            self.commenpost(self.dkserver,self.data)

    #获取销售订单个数
    def getsalebill(self,):
        self.getsalebillserver='ub/standardjc/bill/saleBillJc/statistics'
        self.params=self.e.getsalebillnoparams()
        callresult=self.commenget(self.getsalebillserver,self.params)
        if callresult['resultObject']['count']%10.00 ==0:
            return (int(callresult['resultObject']['count']/10.00))
        else:
            return (int(callresult['resultObject']['count']/10.00+1.00))


    #获取销售订单/id编号列表
    def getsalebilllist(self,billstatus):
        self.getsalebilllistserver='ub/standardjc/bill/saleBillJc/list'
        self.data=self.e.getsalebilllistdata(billstatus)
        callresult = self.commenpost(self.getsalebilllistserver, self.data)
        billidlist=[]
        for pagenum in range(1,int(callresult['resultObject']['totalPage'])):
            self.data['currentPage']=pagenum
            callresult = self.commenpost(self.getsalebilllistserver, self.data)
            for item in callresult['resultObject']['pageData']:
                billidlist.append(item['billId'])
        return (billidlist)


    def getsalebilldetail(self):
        pass

    #销售订单审核
    def examinsalebill(self):
        self.examinsalebillserver='ub/standardjc/bill/saleBillJc/examine'
        self.edata=self.e.examindata()

        billidlist=self.getsalebilllist(1)
        for item in  billidlist:
            self.edata['billId']=item
            print(self.data)
            self.commenpost(self.examinsalebillserver,self.edata)

    #销售订单出库
    def salebillout(self):
        self.salebilloutserver='ub/standardjc/bill/saleOutstockBillJc/add'
        self.surl=os.path.join(self.baseurl,self.salebilloutserver)
        billidlist=self.getsalebilllist(2)
        self.outdata={
            "billId":'',
        }
        for id in billidlist:
            self.outdata['billId']=id
            encodedata=encode_multipart_formdata(self.outdata)
            self.header['Content-Type'] = encodedata[1]
            self.formdata=encodedata[0]
            res=requests.post(url=self.surl,data=self.formdata,headers=self.header).json()
            print(res)

    def salebilloutdemo(self,id):
        self.salebilloutserver='ub/standardjc/bill/saleOutstockBillJc/add'
        self.surl=os.path.join(self.baseurl,self.salebilloutserver)

        self.outdata={
            "billId":'',
        }
        self.outdata['billId']=id

        encodedata=encode_multipart_formdata(self.outdata)
        self.header['Content-Type'] = encodedata[1]
        self.formdata=encodedata[0]

        res=requests.post(url=self.surl,data=self.formdata,headers=self.header).json()
        if res['code']==1:
            print("done")
        else:
            print(res)

    def writebillidtofile(self):
        f=open(r'D:\jemeter\apache-jmeter-5.1.1\data\billid.txt','w')
        self.getsalebilllistserver = 'ub/standardjc/bill/saleBillJc/list'
        self.data = self.e.getsalebilllistdata(3)
        callresult = self.commenpost(self.getsalebilllistserver, self.data)
        for pagenum in range(1, int(callresult['resultObject']['totalPage'])):
            self.data['currentPage'] = pagenum
            callresult = self.commenpost(self.getsalebilllistserver, self.data)
            for item in callresult['resultObject']['pageData']:
                print(item['billId'],type(item['billId']))
                f.write("%s,\n"%item['billId'])
        f.close()




    #多线程跑
    def threaddo(self):
        pool =ThreadPool(10)
        todolist=self.getsalebilllist(2)
        print(todolist,len(todolist))
        request=threadpool.makeRequests(self.salebilloutdemo,todolist)
        [pool.putRequest(req) for req in request]
        pool.wait()


    #销售订单收货
    def acceptbill(self):
        self.acceptbillserver='ub/standardjc/bill/saleBillJc/collect'
        self.aurl= os.path.join(self.baseurl, self.acceptbillserver)
        self.adata={
            "billId":1912171810378002
        }
        billtoaccept=self.getsalebilllist(3)
        for id in billtoaccept:

            self.adata['billId']=id
            encodedata = encode_multipart_formdata(self.adata)
            self.header['Content-Type'] = encodedata[1]
            self.fdata = encodedata[0]
            res = requests.post(url=self.aurl, data=self.fdata, headers=self.header).json()
            print(res)


    #申请销售退货
    def returnbill(self):
        self.returnserver='ub/standardjc/bill/saleReturnBillJc/add'
        self.rdata=self.e.exportsaleReturnBillJc()
        b3 = self.getsalebilllist(3)
        b4=self.getsalebilllist(4)
        b4.append(b3)
        print(b4)
        for id in b4:
            self.rdata['billId']=id
            print(self.rdata)
            self.commenpost(self.returnserver,self.rdata)


    #获取退货订单id
    def getreturnsalebillid(self,billstatus):
        self.getreturnsalebillidserver='ub/standardjc/bill/saleReturnBillJc/list'
        self.params1=self.e.salereurnparams(billstatus)
        res=self.commenpost(self.getreturnsalebillidserver,self.params1)
        count=res['resultObject']['totalPage']
        billidlist=[]
        for pagenum in range(1,count+1):
            self.params1['currentPage']=pagenum
            res=self.commenpost(self.getreturnsalebillidserver,self.params1)
            for item in res['resultObject']['pageData']:
                billidlist.append(item['billId'])

        return billidlist


    #审核销售退货单
    def examinreturnbill(self):
        self.erserver='ub/standardjc/bill/saleReturnBillJc/examine'
        self.erdata={
            "billId": "1912172010060002",
            "billStatus": 2
        }
        billid=self.getreturnsalebillid(1)
        for id in billid:
            self.erdata['billId']=id
            self.commenpost(self.erserver,self.erdata)

    #销售退货单入库
    def returnbillinstock(self):
        self.returnbillinstockserver='ub/standardjc/bill/saleReturnInstockBillJc/add'
        self.rbidata=self.e.exportsaleReturnBillJc()
        returnin=self.getreturnsalebillid(2)
        print(returnin)
        for id in returnin:
            self.rbidata['saleReturnBillId']=id
            self.commenpost(self.returnbillinstockserver,self.rbidata)

    #销售流
    def sale(self):
        self.dkcreatebill()
        print('代客下单申请完')
        self.examinsalebill()
        print('销售订单审核完')
        self.salebillout()
        print('销售订单出库完')
        # time.sleep(5)
        # self.acceptbill()
        # print('销售订单收货完')

    #退货流
    def doreturnbill(self):
        self.returnbill()
        print('销售退货单申请完')
        self.examinreturnbill()
        print('销售退货单审核完')
        self.returnbillinstock()
        print('销售退货单进库完')





if __name__=='__main__':
    e=exportexcl()
    # e.getsalebill()
    # e.getsalebilllist(1)
    # e.examinsalebill()
    # e.salebillout()
    e.writebillidtofile()
    # e.salebillout()
    # e.threaddo()
    # e.sale()
    # e.acceptbill()
    # e.returnbill()
    # e.getreturnsalebillid()
    # e.examinreturnbill()
    # e.returnbillinstock()


