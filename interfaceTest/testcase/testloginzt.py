# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 14:30
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : loginzt.py


from interfaceTest.core import createtest,myhttp
import unittest
import json


d=createtest.testcaseread()
dataget=d.get_xls("login.xls","Sheet1")



class loginzt(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_loginzt(self):
        self.q = myhttp.myhttp()
        for item in dataget:
            self.header=json.loads(item[2])
            self.moethd=item[0]
            self.url=item[1]
            self.data=item[3]
            self.checkcode=item[4]
            self.checkmsg=item[5]
            self.res=self.q.post(headers=self.header,url=self.url,data=self.data).json()
            print(self.res)


if __name__=="__main__":
    unittest.main()








