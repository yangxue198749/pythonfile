#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : SingHandler.py
@Author: yangxue
@Date  : 2019/5/16 10:41
@Desc  : 
'''

from hashlib import md5
import json

class Singhadler:
    def __init__(self):
        pass

    def md5(self,str):
        m=md5()
        m.update(str.encode('utf-8'))
        return (m.hexdigest())


    def sing(self,data):
        list1 = []
        if type(data) !='dict':
            data=json.loads(data)
            for key,values in data.items():
                if key != 'sign' and key != 'skus' and key != 'cards' and key != "days":
                    wd = str(str(key) + '=' + str(values))
                    list1.append(wd)
            list1.sort()
            str1 = str(list1)
            str2 = str1.replace("[", '').replace(']', '').replace("'", '').replace(',', '&').replace(' ', '')
            str3 = str2 + ('&key=test123456789')
            m =self.md5(str3)
            data['sign']=m
        else:
            for key,values in data.items():
                if key != 'sign' and key != 'skus' and key != 'cards' and key != "days":
                    wd = str(str(key) + '=' + str(values))
                    list1.append(wd)
            list1.sort()
            str1 = str(list1)
            str2 = str1.replace("[", '').replace(']', '').replace("'", '').replace(',', '&').replace(' ', '')
            str3 = str2 + ('&key=test123456789')
            m =self.md5(str3)
            data['sign']=m
        return data