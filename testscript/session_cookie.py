# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 9:26
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : session_cookie.py
import requests,os,json


baseurl='https://wmspre.xiyunfin.com/'
url=os.path.join(baseurl,'account/login.do')
data = {
    "account": "yxadmin",
    "password": "y123456",
    "force": 1
}
data=json.dumps(data)
header={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'Content-Type': 'application/json'
}


res=requests.post(url=url,data=data,headers=header,verify=False)
cookies=res.cookies
print(cookies)
s=requests.session()


url2='purchaseBilll/page.do',
url=os.path.join(baseurl,url2)
params={
                   'pageSize':1,
                   'currentPage':1,
                   'totalCount':0,
                   'billNo':None,
                   'supplierNumber':None,
                   'purchaseType':None,
                   'shipperNo':None,
                    'billStatus':None
              }
r=s.request(url=url,method='get',params=params,headers=header,cookies=cookies,verify=False).json()
print(r)
# try:
#     res=requests.post(url=url,headers=header,data=data).json()
#     header['Authorization'] = res['resultObject']['token']
# except Exception as e:
#     print('登陆失败',e)


