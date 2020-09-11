# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 17:42
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : orgchange.py

import requests
import xlrd


class checkorg:

    def __init__(self):
        self.headers = {
            'Authorization': '9e0c50b1a4724f43bae870978a8b84b5',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json;charset=UTF-8'
        }
        self.baseurl=''

    def readxlsx(self,bookname,sheetname,c1,c2,c3):
        checklist=[]
        data=xlrd.open_workbook(bookname)
        table=data.sheet_by_name(sheetname)
        nrow=table.nrows

        for i in range(1,nrow):
            dic1={}
            num=table.cell_value(i,int(c1))
            name=table.cell_value(i,int(c2))
            org=table.cell_value(i,int(c3))
            dic1['num']=num
            dic1['name']=name
            dic1['org']=org
            checklist.append(dic1)
        return checklist

    def checkCustomer(self):
        f=open(r'C:\Users\Think\Desktop\scm一期\custmor.txt','w')
        url='https://scmpre.xiyunfin.com/oms/customer/getPage.do?'
        params={
            'customerNumber': '',
            'enterpriseId':'',
            'localSaleOrgName':'',
            'regionId':'',
            'customerName':'',
            'saleOrgName':'',
            'currentPage':'1',
            'pageSize': '10'
        }
        i = 1
        checklist=self.readxlsx(r'C:\Users\Think\Desktop\scm一期\客户组织架构变更.xlsx','Sheet1','0','1','3')
        for item in checklist:

            # print(item['num'])
            # url='http://crouter.yunzongnet.com/xyscm-backstage/t5050/oms/customer/getPage.do?customerNumber=%s&enterpriseId=&localSaleOrgName=&regionId=&customerName=&saleOrgName=&currentPage=1&pageSize=10'%item['num']
            params['customerNumber']=item['num']

            res=requests.get(url=url,params=params,headers=self.headers).json()
            if res['resultObject']['pageData']:
                if res['resultObject']['pageData'][0]['customerName'] == item['name'] and res['resultObject']['pageData'][0]['localSaleOrgName']==item['org']:
                    print('匹配')
                    f.write('客户编码：%s--客户名称--%s--组织%s----匹配\n'%(res['resultObject']['pageData'][0]['customerNumber'],res['resultObject']['pageData'][0]['customerName'],res['resultObject']['pageData'][0]['localSaleOrgName']))
                    # print('客户编码：%s--客户名称：%s--组织：%s=====不匹配'%(res['resultObject']['pageData'][0]['customerNumber'],res['resultObject']['pageData'][0]['customerName'],res['resultObject']['pageData'][0]['localSaleOrgName']))
                else:
                    f.write('客户编码：%s--客户名称：%s--组织：%s=====不匹配\n'%(res['resultObject']['pageData'][0]['customerNumber'],res['resultObject']['pageData'][0]['customerName'],res['resultObject']['pageData'][0]['localSaleOrgName']))
                    print('不匹配%s'%item['num'])
            #     # time.sleep(0.1)
            else:
                print('数据有误%s'%item['num'])
            i+=1
        f.close()
        print(i)

    def checkSpulier(self):
        f=open(r'C:\Users\Think\Desktop\scm一期\sppulierd.txt','w')
        i=1
        url='https://scmpre.xiyunfin.com/pms/supplier/getPage.do'
        params={
            'supplierNumber':'',
            'supplierName':'',
            'enterpriseId':'',
            'purchaseOrgId':'',
            'contractStatus':'',
            'currentPage':'1',
            'pageSize': '10'
        }
        checklist=self.readxlsx(r'C:\Users\Think\Desktop\scm一期\供应商架构调整.xlsx','Sheet1','0','1','2')
        for item in checklist:
            params['supplierNumber']=item['num']
            # url='http://crouter.yunzongnet.com/xyscm-backstage/t5050/pms/supplier/getPage.do?supplierNumber=%s&supplierName=&enterpriseId=&purchaseOrgId=&contractStatus=&currentPage=1&pageSize=10'%item['num']
            res = requests.get(url=url, params=params,headers=self.headers).json()
            # print(res)
            if res['resultObject']['pageData']:
                supplierId=res['resultObject']['pageData'][0]['supplierId']
                getdetailurl='https://scmpre.xiyunfin.com/pms/supplier/getBaseInfo.do?supplierId=%s'%supplierId
                resdetail=requests.get(url=getdetailurl,headers=self.headers).json()
                orglist=resdetail['resultObject']['purchaseOrgList']
                orgs=[]
                if len(orglist)>0:
                    for orgitem in orglist:
                        orgs.append(orgitem['orgName'])

                    if item['org'] in orgs:
                        f.write('供应商名称:%s---表格中组织：%s---组织列表：%s----匹配\n'%(item['name'],item['org'],orgs))
                        print('匹配---%s---组织列表--%s'%(item['org'],orgs))
                    else:
                        f.write('供应商名称:%s---表格中组织：%s---组织列表：%s----不匹配\n'%(item['name'],item['org'],orgs))
                        print('不匹配---%s'%item['org'])
                else:
                    f.write('数据有误编号--%s\n'%item['org'])
                    print('数据有误，名称%s'%item['org'])
            else:
                f.write('数据有误编号--%s\n'%item['org'])
                print('返回数据有误--%s'%item['org'])
                continue
            i+=1
        f.close()
        print(i)


    def checkpurchaselist(self):
        # 获取一下所有采购价目表数据
        url='https://scmpre.xiyunfin.com/oms/purchasePrice/queryPurchasePriceOfLocalPaging.do'
        params={
            'customerName':'',
            'materialNumber':'',
            'materialName':'',
            'outerMaterialNumber':'',
            'outerMaterialName':'',
            'orgId':'',
            'supplierName':'',
            'belongEpId':'3',
            'currentPage':'1',
            'pageSize':'100'
        }
        clist = []
        for i in range(1,245):
            params['currentPage']=i
            res=requests.get(url=url,params=params,headers=self.headers).json()
            if res['resultObject']['pageData']:
                for item in res['resultObject']['pageData']:
                    dict1={}
                    dict1['customerName']=item['customerName']
                    dict1['orgId']=item['orgId']
                    dict1['orgName']=item['orgName']
                    dict1['orgNumber']=item['orgNumber']
                    # print(item['customerName'])
                    if str(dict1) in clist:
                        pass
                    else:
                        clist.append(str(dict1))

        clist1=set(clist)
        f=open(r'C:\Users\Think\Desktop\scm一期\gaunxi.txt','w')
        for i in clist1:
            f.write('%s\n'%i)
            # print('写入')
        f.close()
        print(len(clist1))
        f=open(r'C:\Users\Think\Desktop\scm一期\purchersh.txt','w')
        checklist = self.readxlsx(r'C:\Users\Think\Desktop\scm一期\客户组织架构变更.xlsx', 'Sheet1','0', '1', '3')
        customerNamelist=[]
        for data in clist1:
            data=eval(data)
            for dt in checklist:
                if data['customerName'] == dt['name']:
                    if data['orgName']  == dt['org']:
                        f.write('接口返回名称组织：(%s-%s)----本地名称/组织：(%s-%s)--匹配\n'%(data['customerName'],data['orgName'],dt['name'],dt['org']))
                    else:
                        f.write('接口返回名称组织：(%s-%s)----本地名称/组织：(%s-%s)--不匹配\n' % (data['customerName'], data['orgName'], dt['name'], dt['org']))
        f.close()

    def checksale(self):
        url='https://scmpre.xiyunfin.com/oms/salePrice/querySalePriceOfLocalPaging.do'
        params={
            'customerName':'',
            'materialNumber':'',
            'materialName':'',
            'orgId':'',
            'currentPage':'1',
            'pageSize':'100'
        }
        clist = []
        for i in range(1, 145):
            params['currentPage'] = i
            res = requests.get(url=url, params=params, headers=self.headers).json()
            if res['resultObject']['pageData']:
                for item in res['resultObject']['pageData']:
                    dict1 = {}
                    dict1['customerName'] = item['customerName']
                    dict1['orgId'] = item['orgId']
                    dict1['orgName'] = item['orgName']
                    dict1['orgNumber'] = item['orgNumber']
                    # print(item['customerName'])
                    if str(dict1) in clist:
                        pass
                    else:
                        clist.append(str(dict1))
        clist1=set(clist)
        f = open(r'C:\Users\Think\Desktop\scm一期\salerelation.txt', 'w')
        for i in clist1:
            f.write('%s\n' % i)
        f.close()

        f = open(r'C:\Users\Think\Desktop\scm一期\sale.txt', 'w')
        customerlist=self.readxlsx(r'C:\Users\Think\Desktop\scm一期\客户组织架构变更.xlsx','Sheet1','0','1','3')
        for data in clist1:
            data=eval(data)
            for item in customerlist:
                if data['customerName']==item['name']:
                    if data['orgName']==item['org']:
                        f.write('接口返回名称组织：(%s-%s)----本地名称/组织：(%s-%s)--匹配\n' % (data['customerName'], data['orgName'], item['name'], item['org']))
                    else:
                        f.write('接口返回名称组织：(%s-%s)----本地名称/组织：(%s-%s)--不匹配\n' % (data['customerName'], data['orgName'], item['name'], item['org']))
        f.close()



if __name__=="__main__":

    c=checkorg()
    # c.checkSpulier()
    # c.checkCustomer()
    # c.checkpurchaselist()
    c.checksale()


