#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : ReadCofig.py
@Author: yangxue
@Date  : 2019/4/28 9:31
@Desc  : 
'''

import configparser
from interfaceTest.log import log
import os


pro_path=os.path.split(os.path.realpath(__file__))[0]
p=os.path.split(pro_path)[0]
cofig_path=os.path.join(p,'config\config.ini')


l=log.log('redcofig','config.txt')

class ReadConfig:
    def __init__(self):
        self.conf=configparser.ConfigParser()
        self.conf.read(cofig_path)

    def get_selection(self):
        try:
            self.selection=self.conf.sections()
        except Exception as e:
            print(e,"这里")
        return self.selection

    def get_opthion(self,name):
        try:
            self.opthions=self.conf.options(name)
        except Exception as e:
            print('get config opthion fail :',e)
        return self.opthions

    def get_item(self,name):
        self.data_dict={}
        try:
            self.items=self.conf.items(name)
            # print(self.items)
            for k in self.items:
                self.data_dict[k[0]]=k[1]
            # l.info('get config item:%s'%self.data_dict)
        except Exception as e:
            l.error('get config fail :',e)
            print('get config fail :',e)
        return self.data_dict


