# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 9:10
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : pullOdersFromK3.py

import requests
import datetime
import os

'''
为了节省拼接参数得方便性，写这个脚本方便一些
1，需要修改得地址 self.baseurl中 https://crouter.yunzongnet.com/xyscm-taskcenter/t5210 目前使用得服务外网地址即可
2，时间自动默认为从本月1号开始，到今天后一天
使用方法：
 可以单个使用，或者多个使用,直接 p.方法名（）即可
'''

class pullOrders:

    def __init__(self):
        self.baseurl='http://t2243.xyscm-taskcenter.yunzong:11515/xyscmx/k3/pull/'
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Content-Type': 'application/json;charset=UTF-8'
        }
        a=datetime.date.today()
        self.start='%s-%s-%s'%(a.year,a.month,'1')
        self.end='%s-%s-%s'%(a.year,a.month,(int(a.day)+1))
        self.params={
            'start':self.start,
            'end':self.end
        }

    #通用方法
    def orderDemo(self,service):
        self.url=os.path.join(self.baseurl,service)
        # print(self.params)
        print(self.url)
        try:
            res=requests.get(url=self.url,params=self.params,headers=self.headers,timeout=20).json()

            print(res)
            return res['success']

        except Exception as e:
            print(e)
    #应收单
    def receivableBill(self):
        result=self.orderDemo('receivableBill.do')
        return result
    #收款单
    def receiptBill(self):
        result=self.orderDemo('receiptBill.do')
        return result

    #暂估应付应付单
    def payableBill(self):
        result=self.orderDemo('payableBill.do')
        return result

    #财务应付单
    def payableAuditBill(self):
        result=self.orderDemo('payableAuditBill.do')
        return result

    #付款单
    def payBill(self):
        result=self.orderDemo('payBill.do')
        return result

    #应付单整流程拉取-
    def payable(self):
        if self.payableBill():
            if self.payableAuditBill():
                self.payBill()

    #应收单整流程拉取
    def reciveable(self):
        if self.receivableBill():
            self.receiptBill()

    #拉取逾期订单
    def overdue(self):
        self.overdueurl='http://t1474.xyscm-taskcenter.yunzong:11515/overdue/bill/update/saleStatus.do'
        a1 = datetime.date.today()
        self.start = '%s-%s-%s' % (a1.year, a1.month, '1')
        self.end = '%s-%s-%s' % (a1.year, a1.month, (int(a1.day) + 1))
        self.params1 = {
            'start': self.start,
            'end': self.end,
            'database':'scm'
        }
        res=requests.get(url=self.overdueurl,params=self.params1,headers=self.headers,timeout=20).json()
        print(res)


if __name__ =='__main__':
    p=pullOrders()
    # p.payableBill()
    # p.payable()
    p.reciveable()
    # p.overdue()
