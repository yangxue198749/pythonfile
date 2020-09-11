#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : mysocket.py
@Author: yangxue
@Date  : 2019/4/29 9:00
@Desc  : 
'''

import socket
from core import ReadCofig
import json
from log import log



socket_link=ReadCofig.ReadConfig().get_item('socket')
logger=log.log('socket','socketlog.log')

class Mysockt:
    def __init__(self):
        self.ip=socket_link['host']
        self.port=socket_link['port']

    def socket_connect(self):
        self.addr=(self.ip,self.port)
        self.conn=socket.socket()
        self.conn.connect(self.addr)

    def socket_send(self,data):
        if type(data) != bytes:
            data=json.dumps(data)
        try:
            self.conn.sendall(data)
        except Exception as e:
            logger.error('fail to send data:%s'%e)

        try:
            self.datarevc=self.conn.recv(1024)
            self.datarevc=json.loads(self.datarevc)
            return self.datarevc
        except Exception as e:
            logger.error(e)
            return None

