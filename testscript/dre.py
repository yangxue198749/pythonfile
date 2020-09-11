# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 11:22
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : dre.py


import  re

def rett(phoneNum):
    before=phoneNum.split('-')
    print(before)
    re1=re.compile("^0\\d{3,4}")
    re2="\\d{7,8}$"
    res=re1.findall(before[0])
    print(res)


    # c = re.compile(r'^[0-9a-zA-Z_-.]+@([0-9a-z]+.)+[a-z]+$', re.I)
    # email = '234234xxx4@qq.com'
    # s = c.search(email)
    # if s:
    #     print(s.group())



rett('010-123456')