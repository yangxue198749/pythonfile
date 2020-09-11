# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 20:19
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : t.py

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

# 采购含税单价
Purchaseprice = 10
# 采购价目表税率
Purchasetaxrate = 13
# 物料分类毛利率
skurateOfmargin = 0.
# 销售价目表税率
Saletaxrate = 9
# 随机数
rand = 0.48

# 不含税单价
realPurchaseprice = float('%.8f'%(Purchaseprice/((100+Purchasetaxrate)/100.00)))
Purchasepricefee = float('%.8f'%((Purchaseprice/((100+Purchasetaxrate)/100.00))*(Purchasetaxrate/100.00)))


print('采购不含税单价= %.6f'%realPurchaseprice)

print('采购税额税额= %.6f'%Purchasepricefee)

# 毛利率
rateOfmargin = float('%.7f'% (1-skurateOfmargin+rand/100.00*2-1/100.00))

print('毛利率= %.6f'%rateOfmargin)

# 销售不含税单价
realSaleprice = float('%.7f' % (realPurchaseprice / rateOfmargin))
print('销售不含税单价= %.6f'%realSaleprice)

# 销售含税单价
salePrice = float('%.7f'%(realSaleprice * ((100 + Saletaxrate) / 100.00)))
print('销售含税单价= %.6f'%salePrice)

salePrice =float('%.7f'%((float('%.7f'%(Purchaseprice/((100 + Purchasetaxrate)/100.00)))/float('%.7f'%(1-skurateOfmargin+rand/100.00*2-1/100.00)))*((100+Saletaxrate)/100.00)))
print('总公式得出销售含税单价= %.5f'%salePrice)
print('总公式得出销售含税单价= %.6f'%salePrice)





