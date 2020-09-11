# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 9:58
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : scriptData.py
import datetime


class Data:
    def __init__(self):
        self.nowdate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.startdate=(datetime.datetime.now()+datetime.timedelta(days=-30)).strftime("%Y-%m-%d %H:%M:%S")
        self.enddate=(datetime.datetime.now()+datetime.timedelta(days=90)).strftime("%Y-%m-%d %H:%M:%S")


    def wdata(self):
        wdata={
            "sponsorName":"杨雪",
            "provinceId":"140000",
            "provinceName":"山西省",
            "districtId":"141002",
            "districtName":"尧都区",
            "cityId":"141000",
            "cityName":"临汾市",
            "detailAddress":"自动创建仓库1",
            "sponsorPhone":"13522069018",
            "orgId":6,
            "orgName":"临汾集采",
            "orgNumber":"203.104",
            "warehouseName":''
        }
        return wdata

    def cdata(self):
        cdata={
            "companyType":0,
            "lastYearIncome":"",
            "socialCreditCode":"123456789123456789",
            "customerName":"测试客户",
            "abbreviations":"CSKH",
            "contactName":"杨雪",
            "warehouseId":185,
            "warehouseName":"脚本创建仓库1",
            "warehouseNumber":"TCKD104654",
            "contractStartDate":"2019-10-01 00:00:00",
            "contractEndDate":"2019-11-30 23:59:59",
            "enterpriseType":2,
            "registerCapital":"100000",
            "setupDate":"2019-10-01 00:00:00",
            "legalPerson":"杨雪",
            "controlPerson":"杨雪",
            "registerProvinceId":"140000",
            "registerProvinceName":"山西省",
            "registerCityId":"141000",
            "registerCityName":"临汾市",
            "registerDistrictId":"141002",
            "registerDistrictName":"尧都区",
            "registerDetailAddr":"饶都",
            "businessTermStart":"",
            "businessTermEnd":"",
            "registStatus":0,
            "businessScope":"一切",
            "contactAddress":"随便",
            "businessCommonFiles":[
                {
                    "type":2,
                    "name":"1.png",
                    "url":"blob:http://t1083.xyscm-biz-manager-web.yunzong:12050/85c96e29-83a0-4d06-8578-555064724cc2",
                    "key":"c446c512a6bf40378ee64eb3b88ebf1a",
                    "uid":1572347248471
                }
            ],
            "legalCommonFiles":[
                {
                    "type":3,
                    "name":"1.png",
                    "url":"blob:http://t1083.xyscm-biz-manager-web.yunzong:12050/7f11faa2-96c2-4601-b6c6-168de803f027",
                    "key":"d505275a1ff0434cb670f36432a0239f",
                    "uid":1572347252832
                }
            ],
            "accountCommonFiles":[

            ],
            "foodSafetyCommonFiles":[
                {
                    "type":11,
                    "name":"1.png",
                    "url":"blob:http://t1083.xyscm-biz-manager-web.yunzong:12050/1bf3abbc-5dbb-4ce3-8965-d495325cb353",
                    "key":"ff79c5cee05046bf955b4e5609d6a6f6",
                    "uid":1572347256801
                }
            ],
            "transactionInvoice":[

            ],
            "businessContract":[

            ],
            "bankName":"北京",
            "accountName":"杨雪",
            "bankCardNumber":"123456789098",
            "alipayAccount":"",
            "customerAddressDOList":[
                {
                    "receiveName":"测试客户",
                    "receivePhone":"13522069018",
                    "provinceId":"140000",
                    "cityId":"141000",
                    "districtId":"141002",
                    "detailAddr":"饶都",
                    "provinceName":"山西省",
                    "districtName":"尧都区",
                    "cityName":"临汾市"
                }
            ],
            "advanceCharge":"",
            "accountPeriod":""
        }
        cdata['contractStartDate']=self.startdate
        cdata['contractEndDate']=self.enddate
        cdata['setupDate']=self.startdate

        return cdata


    def supplier(self):
        sdata={
        "supplierName":"供应商测试",
        "sponsorName":"",
        "registStatus":0,
        "consignProvinceId":"130000",
        "consignProvinceName":"河北省",
        "consignCityId":"130100",
        "consignCityName":"石家庄市",
        "consignDistrictId":"130102",
        "consignDistrictName":"长安区",
        "consignName":"杨雪",
        "consignPhone":"13522069018",
        "consignAddress":"长安区",
        "contactName":"杨雪",
        "contactPhone":"13522069018",
        "contactEmail":"13522069018@qq.coom",
        "contractStartDate":"2019-10-01 00:00:00",
        "contractEndDate":"2019-11-30 23:59:59",
        "socialCreditCode":"123456789456123789",
        "enterpriseType":1,
        "registerCapital":"100000",
        "setupDate":"2019-10-01 00:00:00",
        "legalPerson":"yangxue",
        "controlPerson":"yangxue",
        "registerProvinceId":"130000",
        "registerProvinceName":"河北省",
        "registerCityId":"130100",
        "registerCityName":"石家庄市",
        "registerDistrictId":"130102",
        "registerDistrictName":"长安区",
        "registerDetailAddr":"注册地址",
        "businessTermStart":"",
        "businessTermEnd":"",
        "businessScope":"经营范围",
        "contactAddress":"通讯地址",
        "businessCommonFiles":[
            {
                "type":2,
                "name":"1.png",
                "url":"blob:http://t1083.xyscm-biz-manager-web.yunzong:12050/6bf0cb88-b4c8-49e9-a023-5fb2c391e1a5",
                "key":"c41987aa53644b3badbba09ee1a11a2d",
                "uid":1572417882197
            }
        ],
        "legalCommonFiles":[
            {
                "type":3,
                "name":"1.png",
                "url":"blob:http://t1083.xyscm-biz-manager-web.yunzong:12050/59ae7e29-2954-4df5-ac96-9a8a1b9d2e82",
                "key":"3ae1495f62274e55a6b8176b4a21373a",
                "uid":1572417885655
            }
        ],
        "accountCommonFiles":[

        ],
        "foodSafetyCommonFiles":[
            {
                "type":11,
                "name":"1.png",
                "url":"blob:http://t1083.xyscm-biz-manager-web.yunzong:12050/214cca58-2faa-4820-9a6c-e36e7dd2861b",
                "key":"ed9411fe64de4afa94b4f57b4a75c87d",
                "uid":1572417892233
            }
        ],
        "transactionInvoice":[
            {
                "type":12,
                "name":"1.png",
                "url":"blob:http://t1083.xyscm-biz-manager-web.yunzong:12050/850ab4a2-2ebc-4dfb-b5d5-ad06cf186984",
                "key":"56e155ff6883442aaedc8b72b79f5d80",
                "uid":1572417898151
            }
        ],
        "businessContract":[
            {
                "type":13,
                "name":"1.png",
                "url":"blob:http://t1083.xyscm-biz-manager-web.yunzong:12050/3fe47f58-88ac-4cb1-af91-85e338db8959",
                "key":"cb3be6203898442da72f1c2e8f28f972",
                "uid":1572417901342
            }
        ],
        "bankName":"北京银行",
        "accountName":"北京",
        "bankCardNumber":"1234567489456",
        "alipayAccount":"",
        "rysAccount":"",
        "rongyishouzhanghao":"",
        "warehouseIds":[
            219
        ]
            }
        sdata['contractStartDate']=self.startdate
        sdata['contractEndDate']=self.enddate
        sdata['setupDate']=self.startdate
        return sdata

    def finacaildata(self):
        fdata={
        "fundName":"name",#产品名称
        "fundTypeNo":0,   #产品类型
        "payment":0,      #付款方式？
        "orderForm":0,    #下单方式
        "creditLoop":0,   #是否循环使用
        "settleAccount":0,
        "bondPay":0,
        "waccPay":0,
        "bondRatio":100,
        "costRatio":50,
        "isReplenish":0,
        "costingDay":5,
        "contractPeriod":100,
        "actualPeriod":10,
        "extendBasis":0,
        "etcStepList":"0",
        "beOverdue":100,
        "graceOut":0,
        "isGrace":"1",
        "graceDay":1,
        "graceOverdue":20,
        "graceIn":0,
        "status":0
    }
        return fdata


    def examinedata(self):
        exdata={"id":31,"fundNo":"CP10008","status":1}
        return exdata


    def apprdata(self):
        apprdata={
            "enterpriseId": "213",
            "financeFundList": [
                {
                    "fundTypeNoList": [
                        "0"
                    ]
                }
            ],
            "projectNature": 0
        }


    def perchersedata(self):
        perdata={
            'warehouseNumber':'lf.001' ,
            'materialNumber':'',
            'materialName':'',
            'supplierName':'',
            'createTimeStart':'',
            'createTimeEnd':'',
            'currentPage': 1,
            'pageSize': 50
        }

        return perdata

    def saledata(self):
        saledata={

                "customerId": 1923,
                "customerName": "预发杨雪",
                "customerNumber": "KHA101651",
                "warehouseId": 37,
                "warehouseName": "临汾集采仓",
                "creatorId": 476,
                "creatorName": "杨雪",
                "channelName": "",
                "warehouseNumber": "lf.001",
                "salePriceDetailList": [
                    {
                        "customerId": 1923,
                        "customerName": "预发杨雪",
                        "customerNumber": "KHA101651",
                        "materialName": "(集)丹佳上白高筋小麦粉五得利|1袋*25kg",
                        "materialNumber": "XJC.F01.01.0091",
                        "materialId": 22221,
                        "materialUnitName": "袋",
                        "materialUnitNumber": "009",
                        "materialSpecification": "1袋*25kg",
                        "saleTaxRate": 9,
                        "saleTaxPrice": "15",
                        "saleTaxLocalPrice": "13"
                    }
                ],
                "channelId": 0
            }

        return saledata

    def get_material(self):
        materialdata={
                'pageSize': 10,
                'currentPage': 1,
                'totalCount': 0,
                'materialName': '',
                'groupOneNumber':'',
                'groupTwoNumber':'',
                'groupThreeNumber':''
        }
        return materialdata
if __name__=='__main__':
    d=Data()

