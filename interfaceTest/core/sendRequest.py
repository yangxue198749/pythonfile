# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 17:29
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : sendRequest.py


from core import Readexcle
import requests
import json
class SendRequests():
    def sendRequests(self,s,apiData):
        try:
            #从读取的表格中获取响应的参数作为传递
            method = apiData["method"]

            url = apiData["url"]

            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])

            if apiData["headers"] == "":
                h = None
            else:
                h = apiData["headers"]


            if apiData["data"] == "":
                body_data = None
            else:
                body_data = eval(apiData["data"])

            # type = apiData["type"]

            v = False

            # if type == "json":
            #     body = json.dumps(body_data)
            # if type == "data":
            #     body = body_data
            # else:
            #     body = body_data

            #发送请求
            re = s.request(method=method,url=url,params=par,headers=h,data=body_data,verify=v)
            print(re)
            return re

        except Exception as e:
            print('报错',e)

if __name__ == '__main__':
    s = requests.session()
    testData = Readexcle.ReadExcel.readExcel(r'D:\python\pythonfile\interfaceTest\testfile\login.xls','Sheet1')
    print(testData[1],s)
    response = SendRequests().sendRequests(s,testData[1])
    print(response)