# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 13:57
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : login.py

import requests
import json


class login:
    def __init__(self):
        self.header={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Accept":"application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-Hans-CN;q=1",
            "Content-Type":"application/json",
            "Connection":"keep-alive"
        }
        pass


    def getdata(self):
        data1={
	"tickets": "jwt:eyJhbGciOiJSUzI1NiJ9.eyJpZCI6IjQ2ODEwNDc1IiwianRpIjoiZTZiMWE4ZDg2Y2MyYTZlYjEyNzM0MGNkYWY0MjBkOTg2NGFkZGQzZS0zOm1hbGwiLCJpYXQiOjE1ODE0NzgyNzQ3OTZ9.uaS9Wm2_bwAmStcNy49nJ1GEqoiOMqmArLfvbY-BAWcOLV1j8vLPpU94f66nAQMODS30dEynMz_XsCSZsIunhZUvt1wZrSf4vDPtSuIVqsarxzYuy0GQ_dWpdtVRHDf4BZKhhnpgEvHZm08s7RwHQODLw4BqhOmU6w0Vqffc9Jo",
	"city_id": "1",
	"area_id": "257",
	"company_id": "45661571",
	"_ENV_": {
		"source": "weixin",
		"other_source": "",
		"distribute_channel": "default",
		"platform": "0",
		"device_id": "6e521408-0e83-448d-a497-c13e6fdb6eee",
		"device_name": "",
		"app_version": "2.10.0",
		"os_version": "",
		"appkey_version": "",
		"net": "",
		"mno": "",
		"imei": "",
		"open_id": 0,
		"idfa": "",
		"idfv": "",
		"sn": "",
		"mac": "",
		"ssid": "",
		"bssid": "",
		"lat": 0,
		"lng": 0
	},
	"sale_c2_id": 11,
	"salt_sign": "7CF8AE88175C3D4B2A5E943EE8C97B0F,83,1581494696273"
}
        data=json.dumps(data1)
        res=requests.post(url='https://online.yunshanmeicai.com/mall/api/commodity/getbiandbrand',data=data,headers=self.header,verify=False).json()
        print(res)


    def tudou(self):
        datato={
	"tickets": "jwt:eyJhbGciOiJSUzI1NiJ9.eyJpZCI6IjQ2ODEwNDc1IiwianRpIjoiZTZiMWE4ZDg2Y2MyYTZlYjEyNzM0MGNkYWY0MjBkOTg2NGFkZGQzZS0zOm1hbGwiLCJpYXQiOjE1ODE0NzgyNzQ3OTZ9.uaS9Wm2_bwAmStcNy49nJ1GEqoiOMqmArLfvbY-BAWcOLV1j8vLPpU94f66nAQMODS30dEynMz_XsCSZsIunhZUvt1wZrSf4vDPtSuIVqsarxzYuy0GQ_dWpdtVRHDf4BZKhhnpgEvHZm08s7RwHQODLw4BqhOmU6w0Vqffc9Jo",
	"city_id": "1",
	"area_id": "257",
	"company_id": "45661571",
	"_ENV_": {
		"source": "weixin",
		"other_source": "",
		"distribute_channel": "default",
		"platform": "0",
		"device_id": "6e521408-0e83-448d-a497-c13e6fdb6eee",
		"device_name": "",
		"app_version": "2.10.0",
		"os_version": "",
		"appkey_version": "",
		"net": "",
		"mno": "",
		"imei": "",
		"open_id": 0,
		"idfa": "",
		"idfv": "",
		"sn": "",
		"mac": "",
		"ssid": "",
		"bssid": "",
		"lat": 0,
		"lng": 0
	},
	"sale_c2_id": 11,
	"bi_ids": "14429",
	"salt_sign": "EC5AE1C8A06079FE09B13A094A8E2EFF,70,1581494871836"
}
        data=json.dumps(datato)
        res=requests.post(url="https://online.yunshanmeicai.com/mall/api/search/getsearchlistbybiandbrand",data=data,headers=self.header,verify=False).json()
        print(res)



l=login()

# l.getdata()


l.tudou()