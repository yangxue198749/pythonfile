#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : log.py
@Author: yangxue
@Date  : 2019/4/28 10:38
@Desc  : 
'''


import logging
import logging.handlers
import datetime
import os

base_path=os.path.split(os.path.realpath(__file__))[0]


class log:
    def __init__(self, name,filename):
        self.filepath=os.path.join(base_path,filename)
        self.name = name
        self.filename = self.filepath
        # self.logger=logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        # 生成一个logger对象
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        # 生成haddler,决定输出
        # self.fh = logging.FileHandler(self.filename)
        self.sh = logging.StreamHandler()

        #
        self.fh=logging.handlers.TimedRotatingFileHandler(self.filename,when='midnight',interval=1, backupCount=7,
                                                          atTime=datetime.time(0, 0, 0, 0))

        # 定义formater
        self.fh.setFormatter(logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s"))
        self.sh.setFormatter(logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s"))

        # 绑定handdler
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.sh)



       # return self.logger
    def info(self, msg,*args,**kwargs):
        self.logger.info(msg,*args,*kwargs)

    def debug(self,msg,*args,**kwargs):
        self.logger.debug(msg,*args,**kwargs)

    def error(self,msg,*args,**kwargs):
        self.logger.error(msg,*args,**kwargs)

    def warning(self,msg,*args,**kwargs):
        self.logger.warning(msg,*args,**kwargs)


if __name__ =='__main__':
    l=log('bb','bb.log')
    l.info('q')