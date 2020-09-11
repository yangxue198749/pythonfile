# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 17:10
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : CreateTestData.py

import pymysql

class DataCreate:
    def __init__(self):
        self.sever = 'ts.dev.local.xiyun'
        self.databasename='xyscm_ts'
        self.user='deployment'
        self.password='123456'
        try:
            self.db=pymysql.connect(self.sever,self.user,self.password,self.databasename)
        except Exception as e:
            print('链接数据库失败',e)
        self.cursor =self.db.cursor()


    def insertdata(self,table,name):
        sql="INSERT INTO `xyscmx_ts`.`%s` ( `supplier_name`, `short_name`, `status`, `send_k3`, `third_id`, `supplier_eas_number`, `supplier_number`, `responsible_name`, `responsible_department`, `contact_name`, `contact_phone`, `contact_email`, `consignor_name`, `consignor_phone`, `consign_address`, `enterprise_id`, `enterprise_name`, `enterprise_type`, `contract_start_date`, `contract_end_date`, `contract_status`, `creator_id`, `creator`, `create_time`, `update_time`, `busi_type`) VALUES ('%s', '', '1', '1', '681183', '', '23.017', '师宗县黎彬土豆批发部', '师宗县黎彬土豆批发部', '师宗县黎彬土豆批发部', '15010987655', '15010987655@qq.com', '师宗县黎彬土豆批发部', '15010987655', '师宗县黎彬土豆批发部', '3', '千链', '3', '1970-01-01', '1970-01-01', '2', '0', 'k3', '2019-06-28 13:36:07', '2019-11-12 10:01:13', '0'); "%(table,name)
        self.cursor.execute(sql)
        self.db.commit()


    def selectdata(self):
        sql="select * from scm_customer limit 1"
        self.cursor.execute(sql)
        self.data=self.cursor.fetchall()
        print(self.data)

    def deldata(self):
        pass

    def doinsert(self,num):
        self.name = '测试杨'
        self.table = 'scmx_supplier'
        for i in range(1,int(num)):
            self.name = '测试杨'+str(i)
            self.insertdata(self.table,self.name)
            print('insert success')

    def closedb(self):
        self.db.close()




if __name__=="__main__":
    d=DataCreate()
    d.doinsert(2)
    d.closedb()
