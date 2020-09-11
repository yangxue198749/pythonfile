# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 9:44
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : scfScript.py

from testscript.scriptData import Data
import os
import requests
import json
from urllib3 import encode_multipart_formdata


class scfScript:
    '''
    金融产品管理
    '''
    def __init__(self):
        self.d=Data()
        self.baseurl='http://crouter.yunzongnet.com/scf-backstage/t5670/'
        self.loginservice='scf/user/login'
        self.loginurl=os.path.join(self.baseurl,self.loginservice)
        data={
            "account": "scfyangxue",
            "password": "y123456",
            "platform": 12,
            "force": 1
            }
        self.header={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json'
        }
        self.logindata=json.dumps(data)

        try:
            res=requests.post(url=self.loginurl,data=self.logindata,headers=self.header).json()
            # print(res)
            self.header['Authorization'] = res['resultObject']['token']
        except Exception as e:
            print('登陆失败',e)

    def finacialProductsAdd(self):
        '''
        新增金融产品
        :return:
        '''
        self.addservice='scf/finance/fund/add'
        self.addurl=os.path.join(self.baseurl,self.addservice)
        self.adddata=self.d.finacaildata()
        orderForm={'0':'采购','1':'意向','2':'暂估'}
        gracein={'0':'单笔总额','1':'单笔未结算余额','2':'所有未收款余额','3':'所有未结清总额'}
        for i in (0,1,2):
            for j in (0,1,2,3):
                self.adddata['fundName']='%s-%s-yx'%(orderForm[str(i)],gracein[str(j)])
                self.adddata['orderForm']=i
                self.adddata['graceIn']=j
                self.fdata=json.dumps(self.adddata)
                try:
                    res=requests.post(url=self.addurl,headers=self.header,data=self.fdata).json()
                    print('增加金融产品成功  :',res)
                except Exception as e:
                    print('增加金融产品失败:',e)

    def finacialProductsget(self,pagesize,partname):
        '''
        获取金融产品
        :param pagesize:页面个数
        :param partname: 金融产品搜索词
        :return:
        '''
        self.getservice='scf/finance/fund/page'
        self.geturl=os.path.join(self.baseurl,self.getservice)
        params={
            'pageSize': pagesize,
            'currentPage': 1,
            'totalCount': '',
            'fundNo':'',
            'fundTypeNo':'',
            'fundName':partname,
            'payment':'',
            'settleAccount':'',
            'orderForm':'',
            'effectiveStatus':'',
            'status':''
        }
        try:
            self.getres=requests.get(url=self.geturl,headers=self.header,params=params).json()


        except Exception as e:
            print('获取金融产品失败',e)

    def finacialProductsexamine(self):
        '''
        金融产品审核
        :return:
        '''
        self.examineservice='scf/finance/fund/examine'
        self.examineurl=os.path.join(self.baseurl,self.examineservice)
        self.finacialProductsget(50,'na')  #修改名称和页数
        exdata=self.d.examinedata()
        self.waitexaminedata=[]
        for iterm in self.getres['resultObject']['pageData']:
            if iterm['status']==0:
                dict1={}
                dict1['id']=iterm['id']
                dict1['fundNo']=iterm['fundNo']
                self.waitexaminedata.append(dict1)
        # print(self.waitexaminedata)


        for item1 in self.waitexaminedata:
            exdata['id']=item1['id']
            exdata['fundNo']=item1['fundNo']
            # exdata['status']=item1['status']
            self.exdata=json.dumps(exdata)
            try:
                res=requests.post(url=self.examineurl,headers=self.header,data=self.exdata).json()
                print('审核成功:  ',exdata['fundNo'])
            except Exception as e:
                print('审核不成功:  ',exdata['fundNo'])



class enterpriseManagement:
    '''
    企业管理
    '''

    def __init__(self):
        self.d=Data()
        self.baseurl='http://crouter.yunzongnet.com/scf-backstage/t5670/'
        self.loginservice='scf/user/login'
        self.loginurl=os.path.join(self.baseurl,self.loginservice)
        data={
            "account": "scfyangxue",
            "password": "y123456",
            "platform": 12,
            "force": 1
            }
        self.header={
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json'
        }
        self.logindata=json.dumps(data)

        try:
            res=requests.post(url=self.loginurl,data=self.logindata,headers=self.header).json()
            # print(res)
            self.header['Authorization'] = res['resultObject']['token']
        except Exception as e:
            print('登陆失败',e)

    def getenterprise(self,keyword):
        '''
        获取企业列表
        :return:
        '''
        self.getenterpriseserver='scf/enterprise/page'
        self.getenterpriseurl=os.path.join(self.baseurl,self.getenterpriseserver)
        self.params={
            'pageSize': 50,
            'currentPage': 1,
            'totalCount': '',
            'enterpriseName': keyword,
            'enterpriseNo':'',
            'enterpriseBelong':1,
            'businessStatus':'',
            'effectiveStatus':'',
            'start': 'enterpriseDateStart',
            'end':' enterpriseDateEnd',
            'enterpriseDateStart':'',
            'enterpriseDateEnd':''
        }
        try:
            res=requests.get(url=self.getenterpriseurl,headers=self.header,params=self.params).json()
            # print(res)
        except Exception as e:
            print('获取客户失败',e)

        listdata=[]
        for item in res['resultObject']['pageData']:
            if item['businessStatus']=='0':
                dict1={}
                dict1['enterpriseId']=item['enterpriseId']
                dict1['enterpriseNo']=item['enterpriseNo']
                dict1['enterpriseName']=item['enterpriseName']
                listdata.append(dict1)
        print(listdata)
        return listdata


    def getenterpriseapproval(self):
        '''
        启动立项申请
        :return:
        '''
        self.getenterpriseapprovalservice='scf/enterprise/cAdd'
        self.getenterpriseapprovalurl=os.path.join(self.baseurl,self.getenterpriseapprovalservice)
        listdata=self.getenterprise('')
        self.approvaldata=self.d.apprdata()
        for item in listdata:
            self.approvaldata['enterpriseId']=item['enterpriseId']
            try:
                res=requests.post(url=self.getenterpriseapprovalurl,headers=self.header,data=self.approvaldata)
                print('企业立项申请申请成功',res)
            except Exception as e:
                print('企业立项申请申请失败')

    def requestDing(self):
        '''
        发起钉钉申请
        :return:
        '''
        pass

    def imagedo(self):
        '''
        处理图片信息函数
        主要处理图片上传后返回一个key
        role：钉钉申请：1 供应商：2
        :return:
        '''
        url = os.path.join(self.baseurl, 'scf/oss/file/upload')
        header = {
            'Authorization': '09091ca4b0534cbfb57ff6d49c115d83',
            'Accept-Encoding': 'gzip, deflate'
        }
        filename = '1.png'
        filepath = r'C:\Users\Think\Desktop\img\1.png'
        header['Authorization'] = self.header['Authorization']
        data = {}
        data['type'] = '1'
        data['file'] = (filename, open(filepath, 'rb').read())
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]
        header['Content-Type'] = encode_data[1]
        try:
            res = requests.post(url=url, headers=header, data=data).json()
            key = res['resultObject']['md5']
            print(key)
            return key
        except Exception as e:
            print('图片上传失败', e)








if __name__=="__main__":
    # f=scfScript()
    # # f.finacialProductsAdd()
    # f.finacialProductsexamine()
    e=enterpriseManagement()
    # e.getenterprise('客户')
    e.imagedo()

