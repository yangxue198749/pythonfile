# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 17:23
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : calcLym.py
import random

'''
计算分为3步
计算公式:销售含税单价＝{【采购含税单价/（1+采购价目表税率）】/【（1－物料分类毛利率+Rand（0-1）/100×2－1%）】}×（1+销售价目表税率）
第一步：(四舍五入，保留6位小数)
采购不含税单价=采购含税单价/（1+采购价目表税率）
第二步：(四舍五入，保留6位小数)
毛利率=（1－物料分类毛利率+Rand（0~1）/100×2－1%）
第三步：(四舍五入，保留6位小数)
销售不含税单价=采购不含税单价/毛利率
第四步：(四舍五入，保留2位小数)
销售含税单价=销售不含税单价*（1+销售价目表税率）

名词：1采购不含税单价（realPurchaseprice）2,采购含税单价(Purchaseprice) 3,采购价目表税率(Purchasetaxrate)
4,物料分类毛利率(skurateOfmargin) 5,销售价目表税率(Saletaxrate) 6,毛利率（rateOfmargin）
7,销售不含税单价(realSaleprice) 8,销售含税单价(salePrice)
'''

class claclym:
    def __init__(self):
        # 采购含税单价
        self.Purchaseprice = 110
        # 采购价目表税率
        self.Purchasetaxrate = 10
        # 物料分类毛利率
        self.skurateOfmargin = 0.05
        # 销售价目表税率
        self.Saletaxrate = 13
        # 随机数
        self.rand = 0.02

    def clacstep1(self):
        #不含税单价
        self.realPurchaseprice=float('%.6f'%(self.Purchaseprice/((100+self.Purchasetaxrate)/100.00)))
        print('采购不含税单价= ',self.realPurchaseprice)

    def clacstep2(self):

        #毛利率
        self.rateOfmargin=float('%.6f'%(1-self.skurateOfmargin+self.rand/100.00*2-1/100.00))
        print('毛利率=',self.rateOfmargin)

    def clacstep3(self):
        #销售不含税单价
        self.realSaleprice=float('%.6f'%(self.realPurchaseprice/self.rateOfmargin))
        print('销售不含税单价=',self.realSaleprice)

    def clacstep4(self):

        #销售含税单价
        self.salePrice=('%.6f'%(self.realSaleprice*((100+self.Saletaxrate)/100.00)))
        print('销售含税单价=',self.salePrice)

    def commen(self):

        self.salePrice=float('%.6f'%((float('%.6f'%(self.Purchaseprice/((100+self.Purchasetaxrate)/100.00)))/float('%.6f'%(1-self.skurateOfmargin+self.rand/100.00*2-1/100.00)))*((100+self.Saletaxrate)/100.00)))
        print('总公式得出的销售含税单价=',self.salePrice)

if __name__=='__main__':
    c=claclym()
    c.clacstep1()
    c.clacstep2()
    c.clacstep3()
    c.clacstep4()
    c.commen()


