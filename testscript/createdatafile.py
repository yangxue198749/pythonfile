# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 9:23
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : createdatafile.py


class detesql:

    def insertdata(self,table,name):
        data="INSERT INTO `xyscmx_ts`.`%table` (`supplier_id`, `supplier_name`, `short_name`, `status`, `send_k3`, `third_id`, `supplier_eas_number`, `supplier_number`, `responsible_name`, `responsible_department`, `contact_name`, `contact_phone`, `contact_email`, `consignor_name`, `consignor_phone`, `consign_address`, `enterprise_id`, `enterprise_name`, `enterprise_type`, `contract_start_date`, `contract_end_date`, `contract_status`, `creator_id`, `creator`, `create_time`, `update_time`, `busi_type`) VALUES ('', '%s', '', '1', '1', '681183', '', '23.017', '师宗县黎彬土豆批发部', '师宗县黎彬土豆批发部', '师宗县黎彬土豆批发部', '15010987655', '15010987655@qq.com', '师宗县黎彬土豆批发部', '15010987655', '师宗县黎彬土豆批发部', '3', '千链', '3', '1970-01-01', '1970-01-01', '2', '0', 'k3', '2019-06-28 13:36:07', '2019-11-12 10:01:13', '0'); "%(table,name)
        return data
