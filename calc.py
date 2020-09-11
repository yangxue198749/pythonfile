# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 12:53
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : calc.py


class Clac:
    def __init__(self):
        self.f=0
        self.b=0
        self.i=0
        self.o=0

    def front(self):
        self.f+=1

    def backstage(self):
        self.b+=1

    def interactive(self):
        self.i+=1

    def other(self):
        self.o+=1

    def do(self):
        while 1:
            self.input=input('请输入对应得值，1-基础，2-业务，3-交互，4-订单，5-推出 ：')
            if self.input =='1':
                self.front()
            elif self.input =='2':
                self.backstage()
            elif self.input =='3':
                self.interactive()
            elif self.input =='4':
                self.other()
            elif self.input =='5':
                break
            else:
                print('输入有误')
                continue
        formatresult='''
        基础bug ---%s
        业务bug ---%s
        交互bug ---%s
        订单bug ---%s
        '''%(self.f,self.b,self.i,self.o)
        print(formatresult)

if __name__=="__main__":
    c=Clac()
    c.do()