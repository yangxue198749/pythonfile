# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 10:02
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : exportdata.py

from threadpool import ThreadPool

import threadpool


class Export:
    def __init__(self):
        pass

    def exportsaleBilldata(self):
        #代客下单消息体
        datadk={
                "customerId": 11176,
                "deliveryMode": 0,
                "addressId": 1278,
                "materialList": [
                    {
                        "materialId": 19937,
                        "materialNumber": "gp0001",
                        "materialName": "广平仓库商品",
                        "specification": "ml",
                        "taxRate": 13,
                        "taxPrice": 3.66,
                        "unitNumber": "L",
                        "unitName": "升",
                        "quantity": 1,
                        "allAmount": "3.66"
                    }
                ],
                "billAllAmount": "3.66",
                "isGift": 0,
                "accountTime": 1
            }
        return datadk


    def examindata(self):
        #审核销售订单消息体
        examinsaledata={
                "conversionType": 0,
                "billId": "1912171810378001",
                "status": 1,
                "details": [
                    {
                        "materialId": 19937,
                        "materialNumber": "gp0001",
                        "materialName": "广平仓库商品",
                        "unitNumber": "L",
                        "unitName": "升",
                        "specification": "ml",
                        "taxPrice": 3.66,
                        "taxRate": 13,
                        "saleQuantity": 1,
                        "allAmount": "3.66"
                    }
                ],
                "billAllAmount": "3.66",
                "saleCreditStatus": 0,
                "settlementType": 1,
                "accountTime": 1,
                "examineRemarks": ""
            }
        return examinsaledata

    def getsalebillnoparams(self):
        getsalebilldataparams={

                "billNo":"",
                "customerName": "退货回归客户",
                "groupId": "",
                "billStatus": '',
                "groupName": "",
                "sponsorName":"",
                "settlementType":"",
                "startDate":"",
                "endDate":""
                }


        return getsalebilldataparams

    def getsalebilllistdata(self,billstatus):
        getsalebilllistdata={
            "billNo": "",
            "customerName": "退货回归客户",
            "groupId": "",
            "billStatus": billstatus,
            "groupName": "",
            "sponsorName": "",
            "settlementType": "",
            "startDate": "",
            "endDate": "",
            "currentPage": 1,
            "pageSize": 50,
            "totalCount": 0
        }
        return getsalebilllistdata


    def exportsalerRturnBilldata(self):
        Returnbilldata={
            "saleBillId":"1912171810378012",
            "purchaseCreator":"标集采_千链管理员",
            "purchasePhone":"13800001111",
            "saleRetuenBillDetailParams":[
                {
                    "allAmount":3.66,
                    "materialId":19937,
                    "materialName":"广平仓库商品",
                    "materialNumber":"gp0001",
                    "quantity":1,
                    "returnQuantity":1,
                    "taxPrice":3.66,
                    "taxRate":13,
                    "specification":"ml",
                    "unitName":"升",
                    "unitNumber":"L"
                }
            ],
            "imgInfoList":[

            ],
            "purchaseReason":"ee"
        }
        return Returnbilldata

    def salereurnparams(self,billstatus):
        salereturnparams={

                "billNo":"",
                "srcBillNo":"",
                "customerName":"退货回归客户",
                "billStatus":billstatus,
                "groupName":"",
                "warehouseName":"",
                "startDate":"",
                "endDate":"",
                "currentPage":1,
                "pageSize":10,
                "totalCount":0

        }
        return salereturnparams


    def exportreceivableBillJcdata(self):
        pass

    def exportoverdueBilldata(self):
        pass

    def exportstockdata(self):
        pass

    def exportsaleBillJcOutput(self):
        pass

    def exportsaleReturnBillJc(self):
        salereturnbilldata={
            "saleReturnBillId":"1912192010061152",
            "deliveryMode":0,
            "saleReturnInstockBillDetailParams":[
                {
                    "materialId":19937,
                    "materialName":"广平仓库商品",
                    "materialNumber":"gp0001",
                    "quantity":1,
                    "instockAllAmount":3.66,
                    "instockQuantity":1,
                    "taxPrice":3.66,
                    "taxRate":13,
                    "specification":"ml",
                    "unitName":"升",
                    "unitNumber":"L"
                }
            ]
        }
        return salereturnbilldata









