# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 16:14
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : pullK3commed.py

import datetime

class  command:

    def __init__(self):
        pass

    #生成命令通用函数
    def commenDome(self,filename,server):
        with open(r'D:\python\pythonfile\data\%s.txt'%filename,'w') as fp:
            listcommend=[]
            for month  in range(6,13):     #此处是月份自己控制
                if month in (1,3,5,7,8,10,12):
                    for startday in (1,11,21):
                        if startday == 21:
                            end=startday+10
                            com="curl '127.0.0.1:11515/bh/k3/pull/%s.do?k3AccountCustom=true&start=2019-%d-%d&end=2019-%d-%d'"%(server,month,startday,month,end)
                            listcommend.append(com)
                        else:
                            end=startday+9
                            com="curl '127.0.0.1:11515/bh/k3/pull/%s.do?k3AccountCustom=true&start=2019-%d-%d&end=2019-%d-%d'"%(server,month,startday,month,end)
                            listcommend.append(com)
                elif month==2:
                    for startday in (1, 11, 21):
                        if startday == 21:
                            end = startday + 7             #如果闰年，请手动改成8
                            com = "curl '127.0.0.1:11515/bh/k3/pull/%s.do?k3AccountCustom=true&start=2019-%d-%d&end=2019-%d-%d'" % (
                            server, month, startday, month, end)
                            listcommend.append(com)
                        else:
                            end = startday + 9
                            com = "curl '127.0.0.1:11515/bh/k3/pull/%s.do?k3AccountCustom=true&start=2019-%d-%d&end=2019-%d-%d'" % (
                            server, month, startday, month, end)
                            listcommend.append(com)


                else:
                    for startday in (1,11,21):
                        if startday == 21:
                            end=startday+9
                            com="curl '127.0.0.1:11515/bh/k3/pull/%s.do?k3AccountCustom=true&start=2019-%d-%d&end=2019-%d-%d'"%(server,month,startday,month,end)
                            listcommend.append(com)
                        else:
                            end=startday+9
                            com="curl '127.0.0.1:11515/bh/k3/pull/%s.do?k3AccountCustom=true&start=2019-%d-%d&end=2019-%d-%d'"%(server,month,startday,month,end)
                            listcommend.append(com)
            fp.write(str(listcommend))



    def supplier(self):
        filename = 'supplier'
        server = 'supplier'
        self.commenDome(filename, server)


    def customer(self):
        filename = 'customer'
        server = 'customer'
        self.commenDome(filename, server)

    # 拉取指定时间的销售订单
    def salebill(self):
        filename='salebill'
        server='saleBill'
        self.commenDome(filename,server)

    # 拉取指定时间的采购订单
    def purchesenbill(self):
        filename='purchesenbill'
        server='purchaseBill'
        self.commenDome(filename,server)

    #拉取指定时间的采购入库单
    def purchaseInstockBill(self):
        filename='purchaseInstockBill'
        server='purchaseInstockBill'
        self.commenDome(filename,server)

    # 拉取指定时间的暂估应付单
    def payableBill(self):
        filename = 'payableBill'
        server = 'payableBill'
        self.commenDome(filename, server)

    # 拉取指定时间的财务应付单
    def payableAuditBill(self):
        filename = 'payableAuditBill'
        server = 'payableAuditBill'
        self.commenDome(filename, server)

    # 拉取指定时间的付款单
    def payBill(self):
        filename = 'payBill'
        server = 'payBill'
        self.commenDome(filename, server)

    def saleOutstockBill(self):
        filename = 'saleOutstockBill'
        server = 'saleOutstockBill'
        self.commenDome(filename, server)

    # 拉取指定时间的销售出库单
    def receivableBill(self):
        filename = 'receivableBill'
        server = 'receivableBill'
        self.commenDome(filename, server)

    # 拉取指定时间的应收单
    def receiptBill(self):
        filename = 'receiptBill'
        server = 'receiptBill'
        self.commenDome(filename, server)



    def main(self):
        self.supplier()
        self.customer()
        self.purchesenbill()
        self.payableBill()
        self.receiptBill()
        self.receivableBill()
        self.payBill()
        self.payableAuditBill()
        self.purchaseInstockBill()
        self.salebill()
        self.saleOutstockBill()




if __name__=="__main__":
    c= command()
    c.customer()
    c.supplier()



