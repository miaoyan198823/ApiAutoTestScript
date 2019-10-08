# -*- coding: utf-8 -*-

from api import config_db as db

#根据手机号去更新风控库里运营商认证状态
mobile_certification = "update apply_info set apply_state = '{}' where mobile_phone = '{}'"


#通过手机号设置风控apply_info库里运营商认证状态
def certification_mobile_state(host,phone):
    try:
        sql = mobile_certification .format(1,phone)
        db.db_base(host, sql)
    except Exception as e:
        print("error_info:{}" .format(str(e)))


#修改运营商认证状态
certification_mobile_state('103','136002114455')