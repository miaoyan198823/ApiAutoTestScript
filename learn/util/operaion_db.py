# -*- coding: utf-8 -*-
# @Time : 2019/9/11 14:13
# @Author : miaoyan


import pymysql
import json
from util.operation_json import OperationJson


class OperationDB:
    def __init__(self):
        self.opera_json = OperationJson()
        self.conn = pymysql.connect(
            host = str(self.opera_json.data['db']['host']),
            port = int(self.opera_json.data['db']['port']),
            user = str(self.opera_json.data['db']['user']),
            password = str(self.opera_json.data['db']['password']),
            db = str(self.opera_json.data['db']['db']),
            cursorclass = pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

e
    def search_one(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result_data = self.cursor.fetchall()
            data = json.dumps(result_data,indent=2,sort_keys=True,ensure_ascii=False)
            return data
        except:
            self.conn.rollback()
        self.conn.close()

o = OperationDB()
print(o.search_one("select id,user_name,mobile_phone,password,id_card from user_info where mobile_phone = '13540700000'"))