# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 15:55
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : check.py


body1={
    "accountCommonFiles":"8303b88101c3db9177269b5da367b82c",
    "accountName":"王三",
    "bankCardNumber":621226098733422300,
    "bankName":"北京银行",
    "businessCommonFiles":"57745bc9986f012d623a3c45fe5ce426",
    "businessScope":"水果生鲜",
    "businessTermEnd":"水果生鲜",
    "businessTermStart":"水果生鲜",
    "consignAddress":"北京市丰台区永善里小区001号",
    "consignCityId":110100,
    "consignDistrictId":110101,
    "consignName":"王二",
    "consignPhone":18501922231,
    "consignProvinceId":110000,
    "contactAddress":"北京市丰台区永善里小区001号",
    "contactEmail":"king_dsaf@sina.cn",
    "contactName":"小王",
    "contactPhone":18423312311,
    "contractEndDate":"2028-01-04 00:00:01",
    "contractStartDate":"2018-01-01 00:00:01",
    "controlPerson":"范闲",
    "creatorId":11,
    "creatorName":"小米",
    "deleteImgIds":[
        0
    ],
    "enterpriseNature":0,
    "enterpriseType":3,
    "foodSafetyCommonFiles":"8303b88101c3db9177269b5dawerewrc",
    "imgInfoList":[
        {
            "id":1,
            "key":"dsaffwrewerewrerewrewrwe",
            "name":"大米.jgp",
            "type":1,
            "url":"https://scmx.oss-cn-beijing.aliyuncs.com/underLine/idcard/d9549d4b6f154428b5b28d9dec40d6d9.png"
        }
    ],
    "legalCommonFiles":"7864fd6fb071a393ba774c35eaca3186",
    "legalPerson":"王小石",
    "onlySupplierQuota":0,
    "otherFile":"3b9d190e607a4e6cad14cda1ee96ac37",
    "registStatus":1,
    "registerCapital":100000000,
    "registerCityId":110100,
    "registerDetailAddr":"东城区永善里小区",
    "registerDistrictId":110101,
    "registerProvinceId":110000,
    "setupDate":"2008-01-01 01:10:50",
    "socialCreditCode":1231232131231313,
    "sponsorName":"大王",
    "status":1,
    "strokeQuota":0,
    "subjectIdList":[
        0
    ],
    "supplierId":0,
    "supplierName":"旺旺供应商",
    "supplierNumber":"string",
    "supplierQuota":0
}


body2={
    "accountCommonFiles":None,
    "accountName":"王三",
    "bankCardNumber":621226098733422300,
    "bankName":"北京银行",
    "businessCommonFiles":None,
    "businessScope":"水果生鲜",
    "businessTermEnd":"2028-01-04 00:00:01",
    "businessTermStart":"2028-01-04 00:00:01",
    "consignAddress":"北京市丰台区永善里小区001号",
    "consignCityId":110100,
    "consignDistrictId":110101,
    "consignName":"王二",
    "consignPhone":18501922231,
    "consignProvinceId":110000,
    "contactAddress":"北京市丰台区永善里小区001号",
    "contactEmail":"king_dsaf@sina.cn",
    "contactName":"小王",
    "contactPhone":18423312311,
    "contractEndDate":"2028-01-04 00:00:01",
    "contractStartDate":"2018-01-01 00:00:01",
    "controlPerson":"范闲",
    "creatorId":11,
    "creatorName":"小米",
    "deleteImgIds":[
        0
    ],
    "enterpriseNature":0,
    "enterpriseType":3,
    "foodSafetyCommonFiles":None,
    "imgInfoList":[
        {
            "id":1,
            "key":"dsaffwrewerewrerewrewrwe",
            "name":"大米.jgp",
            "type":1,
            "url":"https://scmx.oss-cn-beijing.aliyuncs.com/underLine/idcard/d9549d4b6f154428b5b28d9dec40d6d9.png"
        }
    ],
    "legalCommonFiles":None,
    "legalPerson":"王小石",
    "onlySupplierQuota":111,
    "otherFile":None,
    "registerCapital":100000000,
    "registerCityId":110100,
    "registerDetailAddr":"东城区永善里小区",
    "registerDistrictId":110101,
    "registerProvinceId":110000,
    "registStatus":1,
    "setupDate":"2008-01-01 01:10:50",
    "socialCreditCode":1231232131231313,
    "sponsorName":"大王",
    "status":1,
    "strokeQuota":123,
    "subjectIdList":[
        0
    ],
    "supplierId":0,
    "supplierName":"旺旺供应商111124332",
    "supplierNumber":"string",
    "supplierQuota":123213
}

for item in body1.keys():
    if item not in body2.keys():
        print(item)
