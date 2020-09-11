# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 15:45
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : wmsscript.py

import requests
import json
import xlrd


class interface:
    def __init__(self):
        self.url='http://t4887.xyscm-biz-warehouse.yunzong:12320/location/add.do'
        self.port='12320'


    def data(self):
        datalist=[]
        data={
    "areaNo":38,
    "locationNo":"BH-HW-00001",
    "forbidStatus":1,
    "locationLong":"",
    "locationWide":"",
    "locationHigh":"",
    "locationWeight":"",
    "locationType":0,
    "areaId":38,
    "warehouseId":1
}

    def posthttp(self):
        data1 = {
            "areaNo": 38,
            "locationNo": "BH-HW-00001",
            "forbidStatus": 1,
            "locationLong": "",
            "locationWide": "",
            "locationHigh": "",
            "locationWeight": "",
            "locationType": 0,
            "areaId": 38,
            "warehouseId": 1
        }
        data2=json.dumps(data1)
        self.header={'Authorization':'Hq4LqHlChQwpvEzHlHeY6A==',
                     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                      'Content-Type':'application/json;charset=UTF-8'
                     }
        res=requests.post(url=self.url,headers=self.header,data=data2)
        print(res.json())

def rexls():
    l=[]
    data=xlrd.open_workbook(r'C:\Users\Think\Desktop\千链商品名称修改20190919.xlsx')
    table=data.sheet_by_name('Sheet1')
    nrow=table.nrows
    print(nrow)
    for i in range(1,nrow):
        # print(table.cell_value(i,1))
        # print(table.cell_value(i,3))
        sql="(UPDATE ba_purchase_price SET material_name ='%s' WHERE material_number ='%s';)"%(table.cell_value(i,3),table.cell_value(i,1))
        # print("(UPDATE ba_purchase_price SET material_name ='%s' WHERE material_number ='%s';)"%(table.cell_value(i,1),table.cell_value(i,3)))
        print(sql.replace('(','').replace(')',''))
        l.append("'UPDATE ba_purchase_price SET material_name ='%s' WHERE material_number ='%s';'"%(table.cell_value(i,1),table.cell_value(i,3)))

# rexls()


from concurrent.futures  import ThreadPoolExecutor
import time

list1=list(range(5))

def say(k):
    if k in list1:
        print('done',k)
    else:
        print('no')

    time.sleep(0.5)

def main():
    st=time.time()
    print(st)
    for i in range(10):
        say(i)
    et=time.time()
    print(et)


    starttime=time.time()
    with ThreadPoolExecutor(10) as executor:
        for i in range(10):
            executor.submit(say,i)
    endtime=time.time()

    print('time=%s'%str(endtime-starttime))
    print('t=%s' % str(et - st))


from urllib3 import encode_multipart_formdata
import requests


def post_files(url, header, data, filename, filepath):
    """
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    """
    data['file'] = (filename, open(filepath, 'rb').read())
    encode_data = encode_multipart_formdata(data)
    data = encode_data[0]
    header['Content-Type'] = encode_data[1]
    r = requests.post(url, headers=header, data=data)
    print(r.content)


if __name__ == "__main__":
    # url,filename,filepath string
    # header,data dict
    # url='http://crouter.yunzongnet.com/xyscm-biz-backstage/t5666/ub/image/cache/upload'
    # header= header={
    #         'Authorization':'d5f15ee7a9b7486cb1ff5f65757b0626',
    #         # 'Content-Type':'multipart/form-data;boundary=----WebKitFormBoundaryxNYitrrLT09kN7Hp',
    #         'Accept-Encoding':'gzip, deflate'
    #     }
    # data={'type':2}
    # filename='1.png'
    # filepath=r'C:\Users\Think\Desktop\img\1.png'
    #
    # print(post_files(url, header, data, filename, filepath))

    data={
    "success":True,
    "code":1,
    "msg":"default success",
    "resultObject":{
        "pageData":[
            {
                "id":49,
                "fundNo":"CP10026",
                "fundName":"意向单-所有未结清订单总额-yx",
                "fundTypeNo":"0",
                "fundTypeName":"厂商配送业务",
                "payment":1,
                "paymentName":"先货后款",
                "orderForm":0,
                "orderFormName":"采购订单",
                "creditLoop":0,
                "creditLoopName":"是",
                "settleAccount":0,
                "settleAccountName":"月结",
                "bondPay":0,
                "bondPayName":"核心企业",
                "waccPay":0,
                "waccPayName":"核心企业",
                "bondRatio":"100",
                "costRatio":"50",
                "isReplenish":0,
                "isReplenishName":"是",
                "costingDay":"5",
                "contractPeriod":"100",
                "actualPeriod":"10",
                "beOverdue":"100",
                "graceOut":"0",
                "isGrace":"1",
                "isGraceName":"有",
                "graceDay":"1",
                "graceOverdue":"20",
                "graceIn":"3",
                "etcStep":None,
                "etcStepName":"有",
                "extendBasis":0,
                "extendBasisName":"到期采购验收单",
                "creatorName":"scf杨雪",
                "createTime":1572925096,
                "effectiveStatus":1,
                "effectiveStatusName":"审核通过",
                "status":0,
                "statusName":"已启用"
            },
            {
                "id":50,
                "fundNo":"CP10027",
                "fundName":"暂估应付单-单笔订单总额-yx",
                "fundTypeNo":"0",
                "fundTypeName":"厂商配送业务",
                "payment":2,
                "paymentName":None,
                "orderForm":0,
                "orderFormName":"采购订单",
                "creditLoop":0,
                "creditLoopName":"是",
                "settleAccount":0,
                "settleAccountName":"月结",
                "bondPay":0,
                "bondPayName":"核心企业",
                "waccPay":0,
                "waccPayName":"核心企业",
                "bondRatio":"100",
                "costRatio":"50",
                "isReplenish":0,
                "isReplenishName":"是",
                "costingDay":"5",
                "contractPeriod":"100",
                "actualPeriod":"10",
                "beOverdue":"100",
                "graceOut":"0",
                "isGrace":"1",
                "isGraceName":"有",
                "graceDay":"1",
                "graceOverdue":"20",
                "graceIn":"0",
                "etcStep":None,
                "etcStepName":"有",
                "extendBasis":0,
                "extendBasisName":"到期采购验收单",
                "creatorName":"scf杨雪",
                "createTime":1572925096,
                "effectiveStatus":1,
                "effectiveStatusName":"审核通过",
                "status":0,
                "statusName":"已启用"
            }
        ],
        "totalCount":41,
        "totalPage":5,
        "nextPage":0
    }
}

    list1=[]
    for iterm in data['resultObject']['pageData']:
        print(iterm,type(iterm))
        dict1 = {}
        dict1['id']=iterm['id']
        list1.append(dict1)
    print(list1)
        # print(iterm[0])




